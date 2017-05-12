import math
import sympy
import sympy.parsing.sympy_parser
from sympy import latex

global X
X = sympy.Symbol('x')


def calcPrecision(ea):
    if ea == 0: return 'Exact'
    if ea >= 0.5: return 0
    return int(-1 * math.log10(2.0 * ea))


def getXCoeff(func, power):
    return func.collect(X).coeff(X ** power)


def mulFunc(func, symbol=None, num=None, func2=None):
    temp = func
    if symbol != None:
        temp = sympy.Mul(temp, sympy.Symbol(symbol))
    if num != None:
        temp = sympy.Mul(temp, sympy.sympify(num))
    if func2 != None:
        temp = sympy.Mul(temp, func2)
    return temp


def addToFunc(func, symbol=None, num=None, func2=None):
    temp = func
    if symbol != None:
        temp = sympy.Add(func, sympy.Symbol(symbol))
    if num != None:
        temp = sympy.Add(func, sympy.sympify(num))
    if func2 != None:
        temp = sympy.Add(temp, func2)
    return temp


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

    func = sympy.parsing.sympy_parser.parse_expr(modifiedExpr)
    if len(list(func.free_symbols)) > 1 or (len(list(func.free_symbols)) == 1 and list(func.free_symbols)[0] != X):
        raise ValueError('Invalid variables used in expression')
    return func


def getLineEquation(point1, point2=(), slope=float("nan")):
    if math.isnan(slope):
        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    c = point1[1] - slope * point1[0]
    return parseExpr(str(slope) + "x+" + str(c))


def toLatex(equation):
    try:
        return (True, latex(parseExpr(str(equation)), mode='inline'))
    except (SyntaxError, ValueError, UnicodeEncodeError, sympy.parsing.sympy_tokenize.TokenError) as e:
        return (False, equation)
