import math

def f(x):
    return math.pow(x,3) + 4 * math.pow(x,2) - 10

def df(x):
    return 3*math.pow(x,2) + 8 * x

def fixed_point(x0, tol, niter):
    fx = f(x0)
    dfx = df(x0)
    error = tol + 1
    cont = 0
    while fx != 0 and error > tol and dfx != 0 and  cont < niter:
        xn = x0 - fx/dfx
        fx = f(xn)
        dfx = df(xn)
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
    elif dfx == 0:
        print str(x0) + " is a posible multiple root"
    else:
        print "failed in " + str(cont) + " iterations"
# 5 cifras: 5 * 10^-5
# 5 decimales: 0.5 * 10^-5
fixed_point(1.5, 0.5 * math.pow(10,-8), 20)
