import timeit

from equation import equation
from resultset import ResultSet
from table import Table
from util import *


def modified_newton_raphson(func, x0, iterations=50, eps=0.00001):
    iterationRows = []
    errors = []
    roots = []
    xi = x0
    boundaries = []
    startTime = timeit.default_timer()

    for i in xrange(iterations):

        xi_1 = xi - (evaluateFunc(func, xi) * evaluateNthDerivative(func, xi, 1)) / (
            evaluateNthDerivative(func, xi, 1)**2 - (evaluateFunc(func, xi) * evaluateNthDerivative(func, xi, 2)))
        # print xi_1, xi

        ea = abs(xi - xi_1)
        ea_rel = abs(xi - xi_1) / max(abs(xi), abs(xi_1))

        iterationRows.append([i + 1, xi, evaluateFunc(func, xi), evaluateNthDerivative(func, xi, 1), xi_1, ea])
        errors.append((i + 1, ea))
        roots.append((i + 1, xi_1))

        xi = xi_1

        if evaluateFunc(func, xi) == 0: ea_rel = 0
        if ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Modified-Newton-Raphson", ['Step', 'xi', 'f(xi)', "f'(xi)", 'xi+1', 'Abs. Error'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea_rel), executionTime, i + 1,
                     equation('x', func), errors=errors, roots=roots, boundaries=boundaries)


# Test
# if __name__ == '__main__':
# stra = "x^5 - 11x^4+46x^3 - 90 * x^2 + 81x - 27"
# stra = "x^3 - 0.165x^2 + 3.993"
# expr = parseExpr(stra)
#
# print modified_newton_raphson(expr, 0.1)


