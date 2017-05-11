import timeit

from resultset import ResultSet
from table import Table
from util import *


def secant(func, x0, x1, iterations=50, eps=0.00001):
    iterationRows = []
    boundaryChordEqn = getLineEquation((x0, evaluateFunc(func, x0)), (x1, evaluateFunc(func, x1)))
    x_prev = x0
    xi = x1
    startTime = timeit.default_timer()

    for i in xrange(iterations):

        xi_1 = xi - evaluateFunc(func, xi) * ((xi - x_prev) / (evaluateFunc(func, xi) - evaluateFunc(func, x_prev)))
        ea = abs(xi - xi_1)
        ea_rel = abs(xi - xi_1) / max(abs(xi_1), abs(xi))

        iterationRows.append([i + 1, x_prev, evaluateFunc(func, x_prev), xi, evaluateFunc(func, xi), xi_1, ea])

        x_prev = xi
        xi = xi_1

        if evaluateFunc(func, xi) == 0: ea_rel = 0
        if ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Secant", ['Step', 'xi-1', 'f(xi-1)', 'xi', 'f(xi)', 'xi+1', 'Abs. Error'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea_rel), executionTime, i + 1, [sympy.lambdify('x', func, 'numpy'),
                                                                          sympy.lambdify('x', boundaryChordEqn,
                                                                                         'numpy')])


# Test
if __name__ == '__main__':
    stra = "e^-x - x"
    expr = parseExpr(stra)

    print secant(1, 1.01, expr)