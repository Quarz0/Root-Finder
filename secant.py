from resultset import ResultSet
from table import Table
from util import *
import timeit


def secant(x0, x1, func, iterations=50, eps=0.00001):
    iterationRows = []
    x_prev = x0
    xi = x1
    startTime = timeit.default_timer()

    for i in xrange(iterations):

        xi_1 = xi - evaluateFunc(func, xi) * ((xi - x_prev) / (evaluateFunc(func, xi) - evaluateFunc(func, x_prev)))
        ea = abs(xi - xi_1) / xi_1

        iterationRows.append([i + 1, x_prev, evaluateFunc(func, x_prev), xi, evaluateFunc(func, xi), xi_1, ea])

        x_prev = xi
        xi = xi_1

        if evaluateFunc(func, xi) == 0: ea = 0
        if ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Secant", ['Step', 'xi-1', 'f(xi-1)', 'xi', 'f(xi)', 'xi+1', 'Ea (%)'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea), executionTime, i + 1, [sympy.lambdify('x', expr, 'numpy'),
                                                                          sympy.lambdify('x', getLineEquation(
                                                                              (x0, evaluateFunc(func, x0)),
                                                                              slope=evaluateNthDerivative(func, x0, 1)),
                                                                                         'numpy')])


# Test

stra = "e^-x - x"
expr = parseExpr(stra)

print secant(1, 1.01, expr)
