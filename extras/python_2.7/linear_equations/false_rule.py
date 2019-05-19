import math

def fun(x):
    return math.exp(-math.pow(x,2)+1) - 4 * math.pow(x,3) + 25

def false_rule(xi, xs, tol, niter):
    fxi = fun(xi)
    fxs = fun(xs)
    if fxi == 0:
        print str(xi) + " is root"
    elif fxs == 0:
        print str(xs) + " is root"
    elif fxi * fxs < 0:
        xm = xi - (fxi*(xs-xi))/(fxs-fxi)
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
            xm = xi - (fxi*(xs-xi))/(fxs-fxi)
            fxm = fun(xm)
            error = abs(xm - aux)
            print error
        if fxm == 0:
            print str(xm) + " is root"
            print "iterations: " + str(cont)
            print "F(X): " + str(fxm)
        elif error <= tol:
            print str(xm) + " is root with tolerance = " + str(tol)
            print "iterations: " + str(cont)
            print "F(X): " + str(fxm)
        else:
            print "failed in "+ str(cont) +" iterations"
    else:
        print "incorrect interval"
#xi = input("enter xi value: ")
#xs = input("enter xs value: ")
#tol = input("enter the tolerance: ")
#niter = input("enter the iterations number: ")
false_rule(1,2,0.001,30)
print fun(1.75)
