import random
import timeit

from fixed_point import fixed_point
from modified_newton_raphson import modified_newton_raphson
from util import *


def general_method(func, iterations=500, eps=0.00001):
    x_coeff = getXCoeff(func, 1)
    g = None
    if x_coeff != 0:
        temp = parseExpr(str(-1.0 * x_coeff) + "*x")
        g = func
        g = addToFunc(g, func2=temp)
        g = mulFunc(g, num=(-1.0 / x_coeff))

    startTime = timeit.default_timer()
    while True:

        x0 = random.randrange(-700000, 700000) / 1000.0

        RS = None
        try:
            if g != None and abs(evaluateNthDerivative(g, x0, 1)) < 1.0:
                RS = fixed_point(func, x0, iterations=iterations, eps=eps)
                if abs(evaluateFunc(func, RS.getRoot())) < 10 ** -5 and RS.getErrors()[-1][1] <= eps:
                    return RS
        except:
            pass

        try:
            RS = modified_newton_raphson(func, x0, iterations=iterations, eps=eps)
            if abs(evaluateFunc(func, RS.getRoot())) < 10 ** -5 and RS.getErrors()[-1][1] <= eps:
                return RS
        except:
            pass

        if (timeit.default_timer() - startTime) > 60:
            raise ValueError('Timeout')


            # print general_method(parseExpr('x^3 - 0.165x^2 + 10^-4 + x'))
