from resultset import ResultSet
from table import Table
from util import *
import timeit


def newton_raphson(x0, func, iterations=50, eps=0.00001):
    iterationRows = []
    xi = x0
    startTime = timeit.default_timer()

    for i in xrange(iterations):

        xi_1 = xi - evaluateFunc(func, xi) / evaluateNthDerivative(func, xi, 1)
        ea = abs(xi - xi_1) / xi_1

        iterationRows.append([i + 1, xi, evaluateFunc(func, xi), evaluateNthDerivative(func, xi, 1), xi_1, ea])

        xi = xi_1

        if evaluateFunc(func, xi) == 0 or ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Newton-Raphson", ['Step', 'xi', 'f(xi)', "f'(xi)", 'xi+1', 'Ea (%)'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea), executionTime, i + 1, [sympy.lambdify('x', expr, 'numpy'),
                                                                          sympy.lambdify('x', getLineEquation(
                                                                              (x0, evaluateFunc(func, x0)),
                                                                              slope=evaluateNthDerivative(func, x0, 1)),
                                                                                         'numpy')])


# Test

stra = "x^5 - 11x^4+46x^3 - 90 * x^2 + 81x - 27"
expr = parseExpr(stra)

print newton_raphson(1.3, expr, eps=0.000001, iterations=100)
