import Incremental_search as inc_s

def f_derivate(point_x,function):
    from scipy.misc import derivative
    return derivative(function, point_x, dx=1e-8)

def f(point_x):
    import math
    #Use dir(math) to know others commands math.exp() math.sin() ...
    return math.pow(point_x,3) + math.pow(point_x,2)



print(f_derivate(1,f))
