import timeit

from equation import equation
from resultset import ResultSet
from table import Table
from util import *


def fixed_point(func, x0, iterations=50, eps=0.00001):
    iterationRows = []
    boundaries = []
    errors = []
    roots = []
    xi = x0
    func = addToFunc(func, 'x')
    startTime = timeit.default_timer()

    for i in xrange(iterations):
        boundaries.append([equation(sympy.lambdify('x', getLineEquation((0, 0), slope=1), 'numpy')), equation(xi, True),
                           equation(
                               sympy.lambdify('x', getLineEquation((0, evaluateFunc(func, xi)), slope=0), 'numpy'))])

        xi_1 = evaluateFunc(func, xi)
        ea = abs(xi - xi_1)
        ea_rel = abs(xi - xi_1) / max(abs(xi), abs(xi_1))

        iterationRows.append([i + 1, xi, xi_1, ea])
        errors.append((i + 1, ea))
        roots.append((i + 1, xi_1))

        xi = xi_1

        if evaluateFunc(func, xi) == 0 or ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Fixed-Point", ['Step', 'xi', 'xi+1', 'Abs. Error'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea_rel), executionTime, i + 1,
                     equation(sympy.lambdify('x', func, 'numpy')),
                     errors=errors, roots=roots, boundaries=boundaries)


# Test

# stra = "x^5 - 11x^4+46x^3 - 90 * x^2 + 81x - 27"
if __name__ == '__main__':
    stra = 'e^-x - x'
    expr = parseExpr(stra)

    print fixed_point(-1.5, expr, eps=0.000001, iterations=100)
