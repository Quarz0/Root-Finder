import numpy as np
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.uic import loadUiType
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from sympy import *

from table import Table

Ui_MainWindow, QMainWindow = loadUiType('window.ui')


def f(x):
    return np.sin(x)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig1 = Figure()
        self.resultsTabWidget.clear()

    def drawFig(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)

    def plot(self, ys):
        plt = self.fig1.add_subplot(111)
        xs = np.arange(-100.0, 100.0, 0.1)
        for y in ys:
            plt.plot(xs, y(xs), c=np.random.rand(3, 1))
        plt.axis([-6, 6, -1, 1])
        # plt.axvline(x=5,c=np.random.rand(3,1))
        self.drawFig(self.fig1)

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
                               QtGui.QTableWidgetItem(QtCore.QString("%1").arg(table.getData()[row][column])))


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    # add table example
    t = Table("test", ["Hi", "there", "man"], [[1, 2, 5], [3, 4, 6]])
    main.drawTable(t)
    main.drawTable(t)

    # figure example
    x = Symbol('x')
    y = sin(x)
    main.plotPoints([0, 1], [0, 0.5])
    main.plot([lambdify(x, y.diff(x), 'numpy'), lambdify(x, sin(x), 'numpy')])

    sys.exit(app.exec_())
