import numpy as np
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.uic import loadUiType
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from sympy import *

from bisection import bisection
from resultset import ResultSet
from table import Table
from util import parseExpr

Ui_MainWindow, QMainWindow = loadUiType('window.ui')


def f(x):
    return np.sin(x)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig1 = Figure()
        self.plt = self.fig1.add_subplot(111)
        self.plt.grid(true)
        # self.plt.axis([-6, 6, -1, 1])
        self.plt.autoscale(true, tight=false)
        self.resultsTabWidget.clear()
        # self.mTw.addWidget()
        self.rootField.setReadOnly(True)
        self.precisionField.setReadOnly(True)

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
        self.drawFig(self.fig1)

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
        qTable = QtGui.QTableWidget()
        self.resultsTabWidget.addTab(qTable, QtCore.QString(table.getTitle()))
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
                               QtGui.QTableWidgetItem(str(('%g' % table.getData()[row][column]))))

    def drawRoot(self, root):
        assert type(root) is float or int, "root is not of type float nor int!: " + str(type(root))
        self.rootField.setText(str(root))

    def drawPrecision(self, precision):
        assert type(precision) is float or int, "precision is not of type float nor int!: " + str(type(precision))
        self.precisionField.setText(str(precision))

    def drawResultSet(self, resultSet):
        assert type(resultSet) is ResultSet, "table is not of type Table!: " + str(type(resultSet))
        self.plotFunctions(resultSet.getEquations())
        self.plotHLines(resultSet.getHLines())
        self.plotVLines(resultSet.getVLines())
        self.drawTable(resultSet.getTable())
        self.drawRoot(resultSet.getRoot())
        self.drawPrecision(resultSet.getPrecision())


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    main.drawResultSet(bisection(0, 0.5, parseExpr("x^3 - 0.165x^2 ")))

    sys.exit(app.exec_())
