import timeit

from resultset import ResultSet
from table import Table
from util import *


def fixed_point(x0, func, iterations=50, eps=0.00001):
    iterationRows = []
    boundaryLineEqn = getLineEquation((0, 0), slope=1)
    xi = x0
    func = addToFunc(func, 'x')
    startTime = timeit.default_timer()

    for i in xrange(iterations):

        xi_1 = evaluateFunc(func, xi)
        ea = abs(xi - xi_1) / abs(xi_1)

        iterationRows.append([i + 1, xi, xi_1, ea])

        xi = xi_1

        if evaluateFunc(func, xi) == 0 or ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Fixed-Point", ['Step', 'xi', 'xi+1', 'Ea (%)'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea), executionTime, i + 1,
                     [sympy.lambdify('x', func, 'numpy'), sympy.lambdify('x', boundaryLineEqn, 'numpy')])


# Test

# stra = "x^5 - 11x^4+46x^3 - 90 * x^2 + 81x - 27"
if __name__ == '__main__':
    stra = 'e^-x - x'
    expr = parseExpr(stra)

    print fixed_point(-1.5, expr, eps=0.000001, iterations=100)
