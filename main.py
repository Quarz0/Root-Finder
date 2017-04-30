import numpy as np
from PyQt4 import QtCore, QtGui, uic
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.pyplot import rcParams
from sympy import *

from resultset import ResultSet
from table import Table

rcParams['mathtext.fontset'] = 'stix'

Ui_MainWindow, QtBaseClass = uic.loadUiType('window2.ui')
Ui_MethodsOptions, QtBaseClass2 = uic.loadUiType('methods_options.ui')


class MathTextLabel(QtGui.QWidget):
    def __init__(self, mathText, parent=None, **kwargs):
        QtGui.QWidget.__init__(self, parent, **kwargs)

        l = QtGui.QVBoxLayout(self)
        l.setContentsMargins(0, 0, 0, 0)

        r, g, b, a = self.palette().base().color().getRgbF()

        self._figure = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
        self._canvas = FigureCanvas(self._figure)
        l.addWidget(self._canvas)

        self._figure.clear()
        text = self._figure.suptitle(
            mathText,
            x=0.0,
            y=1.0,
            horizontalalignment='left',
            verticalalignment='top',
            size=QtGui.QApplication.font().pointSize() * 2)
        self._canvas.draw()

        (x0, y0), (x1, y1) = text.get_window_extent().get_points()
        w = x1 - x0
        h = y1 - y0

        self._figure.set_size_inches(w / 80, h / 80)
        self.setFixedSize(w, h)


class MethodsOptionsWindow(QtGui.QMainWindow, Ui_MethodsOptions):
    def __init__(self, parent=None):
        super(MethodsOptionsWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)


class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.fig1 = Figure()
        self.plt = self.fig1.add_subplot(111)
        self.plt.grid(true)
        self.drawFig(self.fig1)
        # self.plt.axis([-6, 6, -1, 1])
        self.plt.autoscale(true, tight=false)
        self.resultsTabWidget.clear()
        self.methodsButton.clicked.connect(self.handleMethodsButton)
        mathText = r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}}$'
        self.latexLayout.addWidget(MathTextLabel(mathText, self), alignment=QtCore.Qt.AlignHCenter)

    def handleMethodsButton(self):
        window = MethodsOptionsWindow(self)
        window.show()
        window.move(500, 0)

    def initTableWidget(self):
        qWidget = QtGui.QWidget()
        qVbox = QtGui.QVBoxLayout()
        qTable = QtGui.QTableWidget()
        qTable.setObjectName("Table")
        qWidget2 = QtGui.QWidget()
        hBox = QtGui.QHBoxLayout()
        hBox.setMargin(0)
        rootLabel = QtGui.QLabel()
        rootLabel.setText("Root")
        rootField = QtGui.QLineEdit()
        rootField.setObjectName("Root")
        rootField.setReadOnly(True)
        hBox.addWidget(rootLabel)
        hBox.addWidget(rootField)
        qWidget2.setLayout(hBox)
        qWidget3 = QtGui.QWidget()
        hBox2 = QtGui.QHBoxLayout()
        hBox2.setMargin(0)
        precisionLabel = QtGui.QLabel()
        precisionLabel.setText("Precision")
        precisionField = QtGui.QLineEdit()
        precisionField.setObjectName("Precision")
        precisionField.setReadOnly(True)
        timeLabel = QtGui.QLabel()
        timeLabel.setText("Time")
        timeField = QtGui.QLineEdit()
        timeField.setObjectName("Time")
        timeField.setReadOnly(True)
        hBox2.addWidget(precisionLabel)
        hBox2.addWidget(precisionField)
        hBox2.addWidget(timeLabel)
        hBox2.addWidget(timeField)
        qWidget3.setLayout(hBox2)
        qVbox.addWidget(qTable)
        qVbox.addWidget(qWidget2)
        qVbox.addWidget(qWidget3)
        qWidget.setLayout(qVbox)
        return qWidget

    def drawFig(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)

    def plotFunctions(self, functions):
        xs = np.arange(-100.0, 100.0, 0.1)
        for function in functions:
            self.plt.plot(xs, function(xs), c=np.random.rand(3, 1))

    def plotVLines(self, vLines):
        assert type(vLines) is list, "vLines is not of type list!: " + str(type(vLines))
        for line in vLines:
            self.plt.axvline(x=line, c=np.random.rand(3, 1))

    def plotHLines(self, hLines):
        assert type(hLines) is list, "hLines is not of type list!: " + str(type(hLines))
        for line in hLines:
            self.plt.axhlne(y=line, c=np.random.rand(3, 1))

    def plotPoints(self, xs, ys):
        plt = self.fig1.add_subplot(111)
        for i in range(len(xs)):
            plt.scatter(xs[i], ys[i], marker="x", s=100, c=np.random.rand(3, 1))

    def drawTable(self, table):
        assert type(table) is Table, "table is not of type Table!: " + str(type(table))
        qWidget = self.initTableWidget()
        self.resultsTabWidget.addTab(qWidget, QtCore.QString(table.getTitle()))
        qTable = self.resultsTabWidget.findChild(QtGui.QTableWidget, "Table")
        setattr(self, 'Table%d' % self.resultsTabWidget.count(), qTable)

        qTable.setColumnCount(len(table.getHeader()))
        qTable.setHorizontalHeaderLabels(table.getHeader())
        qTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        qTable.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        qTable.setSelectionMode(QtGui.QTableWidget.SingleSelection)

        qTable.setRowCount(len(table.getData()))
        for row in xrange(len(table.getData())):
            for column in xrange(len(table.getHeader())):
                qTable.setItem(row, column,
                               QtGui.QTableWidgetItem(str(('%g' % table.getData()[row][column]) if type(
                                   table.getData()[row][column]) is float else table.getData()[row][column])))

        return qWidget

    def drawRoot(self, root, rootField):
        assert type(root) is float or int, "root is not of type float nor int!: " + str(type(root))
        assert type(rootField) is QtGui.QLineEdit, "rootField is not of type QtGui.QLineEdit!: " + str(type(rootField))
        rootField.setText(str(root))

    def drawPrecision(self, precision, precisionField):
        assert type(precision) is float or int, "precision is not of type float nor int!: " + str(type(precision))
        assert type(precisionField) is QtGui.QLineEdit, "precisionField is not of type QtGui.QLineEdit!: " + str(
            type(precisionField))
        precisionField.setText(str(precision))

    def drawTime(self, time, timeField):
        assert type(time) is float or int, "time is not of type float nor int!: " + str(type(time))
        assert type(timeField) is QtGui.QLineEdit, "timeField is not of type QtGui.QLineEdit!: " + str(type(timeField))
        timeField.setText(str(('%g' % time)))

    def drawResultSet(self, resultSet):
        assert type(resultSet) is ResultSet, "table is not of type Table!: " + str(type(resultSet))
        self.plotFunctions(resultSet.getEquations())
        self.plotHLines(resultSet.getHLines())
        self.plotVLines(resultSet.getVLines())
        qWidget = self.drawTable(resultSet.getTable())
        self.drawRoot(resultSet.getRoot(), qWidget.findChild(QtGui.QLineEdit, "Root"))
        self.drawPrecision(resultSet.getPrecision(), qWidget.findChild(QtGui.QLineEdit, "Precision"))
        self.drawTime(resultSet.getExecutionTime(), qWidget.findChild(QtGui.QLineEdit, "Time"))


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    main.showMaximized()
    # main.drawResultSet(false_position(-5, 5, parseExpr("x^3 ")))

    sys.exit(app.exec_())
