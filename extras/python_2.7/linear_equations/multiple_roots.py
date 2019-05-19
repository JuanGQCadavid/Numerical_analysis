import math

def f(x):
    return math.pow(x,4) - 18 * math.pow(x,2) + 81

def df(x):
    return 4 * math.pow(x,3) - 36 * x

def d2f(x):
    return 12 * math.pow(x,2) - 36

def multiple_roots(x0, tol, niter):
    fx = f(x0)
    error = tol + 1
    cont = 0
    den = math.pow(df(x0),2) - fx * d2f(x0)
    while fx != 0 and error > tol and den != 0 and cont < niter:
        xn = x0 - (fx*df(x0))/den
        fx = f(xn)
        error = abs((xn-x0)/xn)
        cont = cont + 1        
        x0 = xn
        den = math.pow(df(x0),2) - fx * d2f(x0)
    if fx == 0:
        print str(x0) + " is a root"
        print "iterations: " + str(cont)
        print "F(X): " + str(fx)
        print "F'(X): " + str(df(x0))
        print "F''(X): " + str(d2f(x0))
        print "error: " + str(error)
    elif error <= tol:
        print str(x0) + " is a root with tolerance = " + str(tol)
        print "iterations: " + str(cont)
        print "F(X); " + str(fx)
        print "error: " + str(error)
    else:
        print "failed in " + str(cont) + " iterations"
# 5 cifras: 5 * 10^-8
# 5 decimales: 0.5 * 10^-8
multiple_roots(-2.5, 0.5 * math.pow(10,-8), 20)
