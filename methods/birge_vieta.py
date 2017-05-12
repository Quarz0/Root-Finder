from math import fabs
from sympy import Poly, degree
from sympy.abc import x

from util import *


def birge_vieta(func, xa, iterations=100, eps=0.00001):
    coeff = Poly(func, x).all_coeffs()
    deg = degree(func, gen=x)

    sol = []

    if deg <= 1:
        return

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
    print sol


def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * 10 ** -4


if __name__ == '__main__':
    str = 'x^3-x^2-x+1'
    expr = parseExpr(str)

    birge_vieta(expr, 0.5)
