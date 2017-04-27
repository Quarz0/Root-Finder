import timeit

from resultset import ResultSet
from table import Table
from util import *


def bisection(xl, xu, func, iterations=50, eps=0.00001):
    if evaluateFunc(func, xl) * evaluateFunc(func, xu) > 0:
        return float('nan')

    boundaryLines = [xl, xu]
    iterationRows = []
    startTime = timeit.default_timer()

    for i in xrange(iterations):
        xr = (xu + xl) / 2
        ea = abs(1.0 * (xu - xl) / max(abs(xu), abs(xl)))

        iterationRows.append([i + 1, xl, evaluateFunc(func, xl), xu, evaluateFunc(func, xu), xr, ea])

        if evaluateFunc(func, xl) * evaluateFunc(func, xr) < 0:
            xu = xr
        else:
            xl = xr

        if evaluateFunc(func, xl) * evaluateFunc(func, xr) == 0: ea = 0
        if ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Bisection", ['Step', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'Ea (%)'], iterationRows)

    return ResultSet(table, xr, calcPrecision(ea), executionTime, i, [sympy.lambdify('x', func, 'numpy')],
                     vLines=boundaryLines)


# Test

def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** -4


if __name__ == '__main__':
    str = 'x^3 - 0.165x^2 + 10^-4'
    expr = parseExpr(str)

    print bisection(0.00, 0.11, expr)
