import timeit
from math import fabs
from sympy import Poly, degree
from sympy.abc import x

from equation import equation
from resultset import ResultSet
from table import Table
from util import *


def birge_vieta(func, xa, iterations=50, eps=0.00001):
    coeff = Poly(func, x).all_coeffs()
    deg = degree(func, gen=x)
    coeff = [float(i) for i in coeff]
    sol = [xa]
    iterationRows = []
    errors = []
    roots = []

    if deg <= 1:
        return
    startTime = timeit.default_timer()
    for i in xrange(iterations):
        b = [coeff[0]]
        for j in xrange(len(coeff) - 1):
            b.append((xa * b[j]) + coeff[j + 1])
        c = [coeff[0]]
        for j in xrange(len(coeff) - 2):
            c.append((xa * c[j]) + coeff[j + 1])
        xa -= b[len(b) - 1] / c[len(c) - 1]
        sol.append(xa)
        if fabs(1 - sol[len(sol) - 2] / xa) <= eps:
            break

    executionTime = timeit.default_timer() - startTime

    x_old = None
    for i in xrange(len(sol)):
        if x_old != None:
            ea = abs(sol[i] - x_old)
            ea_rel = abs(sol[i] - x_old) / max(abs(x_old), abs(sol[i]))
        else:
            ea = "-"
        iterationRows.append([i + 1, sol[i], evaluateFunc(func, sol[i]), ea])
        errors.append((i + 1, ea))
        roots.append((i + 1, sol[i]))
        x_old = sol[i]

    table = Table("Birge-Vieta", ['Step', 'xi', 'f(xi)', 'Abs. Error'], iterationRows)

    return ResultSet(table, x_old, calcPrecision(ea_rel), executionTime, len(sol),
                     equation(func), errors=errors, roots=roots, boundaries=[])


def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** -4


if __name__ == '__main__':
    str = 'x^3 -5*x + 6'
    expr = parseExpr(str)
    #
    print birge_vieta(expr, 0)
