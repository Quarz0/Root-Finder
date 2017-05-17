import timeit

from equation import equation
from resultset import ResultSet
from table import Table
from util import *


def newton_raphson(func, x0, iterations=50, eps=0.00001):
    iterationRows = []
    errors = []
    roots = []
    xi = x0
    boundaries = []
    startTime = timeit.default_timer()

    for i in xrange(iterations):
        boundaries.append([equation(
            getLineEquation((xi, evaluateFunc(func, xi)), slope=evaluateNthDerivative(func, xi, 1)))])

        xi_1 = xi - evaluateFunc(func, xi) / evaluateNthDerivative(func, xi, 1)
        ea = abs(xi - xi_1)
        ea_rel = abs(xi - xi_1) / max(abs(xi), abs(xi_1))

        iterationRows.append([i + 1, xi, evaluateFunc(func, xi), evaluateNthDerivative(func, xi, 1), xi_1, ea])
        errors.append((i + 1, ea))
        roots.append((i + 1, xi_1))

        xi = xi_1

        if evaluateFunc(func, xi) == 0: ea_rel = 0
        if ea < eps: break

    executionTime = timeit.default_timer() - startTime
    table = Table("Newton-Raphson", ['Step', 'xi', 'f(xi)', "f'(xi)", 'xi+1', 'Abs. Error'], iterationRows)

    return ResultSet(table, xi, calcPrecision(ea_rel), executionTime, i + 1,
                     equation('x', func), errors=errors, roots=roots, boundaries=boundaries, errorBound=abs(
            ((x0 - xi) ** 2 * evaluateNthDerivative(func, x0, 2)) / (2.0 * evaluateNthDerivative(func, x0, 1))))


# Test
if __name__ == '__main__':
    # stra = "x^5 - 11x^4+46x^3 - 90 * x^2 + 81x - 27"
    stra = "x^3 - 0.165x^2 + 3.993"
    expr = parseExpr(stra)

    print newton_raphson(1.3, expr, eps=0.000001, iterations=100)
