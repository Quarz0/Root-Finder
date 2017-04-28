import math
import sympy
import sympy.parsing.sympy_parser

global X
X = sympy.Symbol('x')


def calcPrecision(ea):
    if ea == 0: return 'Exact'
    return int(2.0 - math.log10(2.0 * ea))


def addToFunc(func, expr):
    return sympy.Add(func, sympy.Symbol(expr))


def evaluateFunc(f, val):
    return sympy.N(f.subs({X: val}))


def evaluateNthDerivative(f, val, n):
    return sympy.N(sympy.diff(f, X, n).subs({X: val}))


def parseExpr(expr):
    modifiedExpr = ""
    for c in expr.lower().replace('^', '**'):
        if c >= 'a' and c <= 'z':
            if len(modifiedExpr) > 0 and modifiedExpr[-1] >= '0' and modifiedExpr[-1] <= '9':
                modifiedExpr += '*'
            if c == 'e':
                modifiedExpr += "E"
            else:
                modifiedExpr += c
        else:
            modifiedExpr += c
    return sympy.parsing.sympy_parser.parse_expr(modifiedExpr)


def getLineEquation(point1, point2=(), slope=float("nan")):
    if slope == float("nan"):
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    c = point1[1] - slope * point1[0]
    return parseExpr(str(slope) + "x+" + str(c))
