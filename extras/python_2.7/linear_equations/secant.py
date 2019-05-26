import math

def f(x):
    return math.pow(x,3) + 4 * math.pow(x,2) - 10

def secant(x0, x1, tol, niter):
    fx0 = f(x0)
    if fx0 == 0:
        print str(x0) + " is a root"
    fx1 = f(x1)
    error = tol + 1
    cont = 0
    den = fx1 - fx0
    while fx1 != 0 and error > tol and den != 0 and  cont < niter:
        x2 = x1 - fx1*(x1-x0)/den
        error = abs((x2-x1)/x2)
        cont = cont + 1
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x1)           
        den = fx1 - fx0
    if fx1 == 0:
        print str(x0) + " is a root"
        print "iterations: " + str(cont)
        print "F(X); " + str(fx1)
        print "error: " + str(error)
    elif error <= tol:
        print str(x0) + " is a root with tolerance = " + str(tol)
        print "iterations: " + str(cont)
        print "F(X): " + str(fx1)
        print "error: " + str(error)
    elif den == 0:
        print str(x0) + " is a posible multiple root"
    else:
        print "failed in " + str(cont) + " iterations"
# 5 cifras: 5 * 10^-5
# 5 decimales: 0.5 * 10^-5
secant(1.3, 1.4, math.pow(10,-8), 20)
