import timeit
from math import fabs
from sympy import Poly, degree
from sympy.abc import x
from resultset import ResultSet
from equation import equation
from table import Table

from util import *


def birge_vieta(func, xa, iterations=50, eps=0.00001):
    coeff = Poly(func, x).all_coeffs()
    deg = degree(func, gen=x)

    sol = [xa]
    iterationRows = []
    errors = []
    roots = []

    if deg <= 1:
        return

    startTime = timeit.default_timer()
    for i in xrange(deg, 1, -1):
        for j in xrange(1, iterations + 1):
            p = coeff[0]
            d = p
            for k in xrange(1, i):
                p = p * xa + coeff[k]
                d = d * xa + p
            p = p * xa + coeff[i]
            d = -p / d if d else -p
            xa += d
            if fabs(d) <= eps * fabs(xa):
                break
        if j == iterations:
            break

        sol.append(xa)

        for k in xrange(1, i):
            coeff[k] += coeff[k - 1] * xa

    sol.append(-coeff[1] / coeff[0])
    executionTime = timeit.default_timer() - startTime

    x_old = None
    for i in xrange(len(sol)):
        if x_old != None:
            ea = abs(sol[i] - x_old)
            ea_rel = abs(sol[i] - x_old) / max(abs(x_old), abs(sol[i]))
        else:
            ea = "-"
        iterationRows.append([i+1, sol[i], evaluateFunc(func, sol[i]), ea])
        errors.append((i+1, ea))
        roots.append((i+1, sol[i]))
        x_old = sol[i]

    table = Table("Birge-Vieta", ['Step', 'xi', 'f(xi)', 'Abs. Error'], iterationRows)

    return ResultSet(table, x_old, calcPrecision(ea_rel), executionTime, len(sol),
                     equation(func), errors=errors, roots=roots, boundaries=[])


def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** -4


if __name__ == '__main__':
    str = 'x^3-x^2-x+1'
    expr = parseExpr(str)
#
    print birge_vieta(expr, 0.5)
