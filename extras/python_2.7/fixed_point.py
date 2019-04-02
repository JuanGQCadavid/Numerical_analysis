import math

def f(x):
    return x * math.exp(x) - math.pow(x,2) - 5*x - 3

def g(x):
    return (x * math.exp(x) - math.pow(x,2) - 3)/5

def fixed_point(x0, tol, niter):
    fx = f(x0)
    error = tol + 1
    cont = 0
    while fx != 0 and error > tol and cont < niter:
        xn = g(x0)
        fx = f(xn)
        error = abs((xn-x0)/xn)
        cont = cont + 1
        x0 = xn
    if fx == 0:
        print str(x0) + " is a root"
        print "iterations: " + str(cont)
        print "F(X); " + str(fx)
        print "error: " + str(error)
    elif error <= tol:
        print str(x0) + " is a root with tolerance = " + str(tol)
        print "iterations: " + str(cont)
        print "F(X): " + str(fx)
        print "error: " + str(error)
    else:
        print "failed in " + str(cont) + " iterations"
# 5 cifras: 5 * 10^-5
# 5 decimales: 0.5 * 10^-5
fixed_point(-0.5, 5 * math.pow(10,-5), 20)
