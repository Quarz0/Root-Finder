import timeit

from resultset import ResultSet
from table import Table
from util import *
from equation import equation


def bisection(func, xl, xu, iterations=50, eps=0.00001):
    if evaluateFunc(func, xl) * evaluateFunc(func, xu) > 0:
        return float('nan')

    boundaryLines = []
    iterationRows = []
    startTime = timeit.default_timer()
    xr_old = None

    for i in xrange(iterations):
        boundaryLines.append([equation(xl, True), equation(xu, True)])
        xr = (xu + xl) / 2

        if xr_old != None:
            ea = abs(xr - xr_old)
            ea_rel = abs(xr - xr_old) / max(abs(xr_old), abs(xr))
        else:
            ea = "-"

        iterationRows.append([i + 1, xl, evaluateFunc(func, xl), xu, evaluateFunc(func, xu), xr, ea])
        xr_old = xr

        if evaluateFunc(func, xl) * evaluateFunc(func, xr) < 0:
            xu = xr
        else:
            xl = xr

        if evaluateFunc(func, xl) * evaluateFunc(func, xr) == 0:
            ea_rel = 0
            break
        if i > 0 and ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Bisection", ['Step', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'Abs. Error'], iterationRows)

    return ResultSet(table, xr, calcPrecision(ea_rel), executionTime, i, [equation(sympy.lambdify('x', func, 'numpy'))],
                     boundaries=boundaryLines)


# Test

def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** -4


# if __name__ == '__main__':
str = 'x^3 - 0.165x^2 + 10^-4'
expr = parseExpr(str)

print bisection(expr, 0.00, 0.11)
