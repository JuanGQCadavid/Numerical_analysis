import math

def fun(x):
    return math.exp(x+3) + math.pow(x,3)/3 - 10

def bisection(xi, xs, tol, niter):
    fxi = fun(xi)
    fxs = fun(xs)
    if fxi == 0:
        print str(xi) + " is root"
    elif fxs == 0:
        print str(xs) + " is root"
    elif fxi * fxs < 0:
        xm = (xi + xs) / 2.0
        fxm = fun(xm)
        cont = 1
        error = tol + 1
        while fxm != 0 and error > tol and cont < niter:
            if (fxi * fxm) < 0:
                xs = xm
                fxs = fun(xs)
            else:
                xi = xm
                fxi = fun(xi)
            cont = cont + 1
            aux = xm
            print "aux: " + str(aux)
            xm = (xi + xs) / 2.0
            print "xm: " + str(xm)
            fxm = fun(xm)
            error = abs(xm - aux)
            print error
        if fxm == 0:
            print str(xm) + " is root"
        elif error <= tol:
            print cont
            print str(xm) + " is root with tolerance = " + str(tol)
        else:
            print "failed in "+ str(cont) +" iterations"
    else:
        print "incorrect interval"
#xi = input("enter xi value: ")
#xs = input("enter xs value: ")
#tol = input("enter the tolerance: ")
#niter = input("enter the iterations number: ")
bisection(-1,0,10e-6,30)
