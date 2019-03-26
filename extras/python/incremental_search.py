# exp() and
import math
# Function definition: e(3x-12) + x * cos(3*x) - x2 + 4
def fun(x):
 return math.exp(3*x - 12) + x * math.cos(3*x) - pow(x, 2) + 4

def incremental_search(xi, fxi):
 global cont
 xs = xi + delta
 fxs = fun(xs)
 print "x   y"
 print str(xi) + " " + str(fxi) 
 while fxi*fxs > 0 and cont < m_iter:
  xi = xs
  fxi = fxs
  xs = xi + delta
  fxs = fun(xs)
  cont = cont + 1
  print str(xs) + " " + str(fxs) 
 if fxs == 0:
  print str(xs) + " is a root"
 elif fxi*fxs < 1:
  print str("there is a root in ["+ str(xi) +","+ str(xs) +"]")
  return xs
 else:
  print str("failed in "+ str(cont) +" iterations")
 return None

xi = input("enter the initial value: ")
delta = input("enter the delta value: ")
m_iter = input("enter the iterations number: ")
fxi = fun(xi)
if fxi == 0:
 print str(xi)+str(" is root")
else:
 cont = 1
 xa = incremental_search(xi, fxi)
 while xa != None:
  cont = cont + 1
  fxa = fun(xa)
  xa = incremental_search(xa, fxa) 
