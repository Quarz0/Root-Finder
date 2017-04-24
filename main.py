import numpy as np
from PyQt4 import QtGui
from PyQt4.uic import loadUiType
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from sympy import *

Ui_MainWindow, QMainWindow = loadUiType('window.ui')


def f(x):
    return np.sin(x)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig1 = Figure()

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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    # figure example
    x = Symbol('x')
    y = sin(x)
    main.plotPoints([0, 1], [0, 0.5])
    main.plot([lambdify(x, y.diff(x), 'numpy'), lambdify(x, sin(x), 'numpy')])

    sys.exit(app.exec_())
