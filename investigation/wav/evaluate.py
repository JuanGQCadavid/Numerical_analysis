import numpy as np

def abserrors(realy, restoredy, matches=None):
    """
    Computes the absolute errors of realy comparing it to restoredy.
    If matches provided it returns only those in which matches[i] == False
    """
    if matches == None:
        return [abs(float(y0) - float(y1)) for (y0, y1) in zip(realy, restoredy)]
    else:
        return [abs(float(y0) - float(y1)) for (y0, y1, match) in zip(realy, restoredy, matches) if not match]

def relerrors(realy, restoredy, matches=None, scalator=0):
    """
    Calculates the relative errors comparing each restored value with it's real value
    and centering the function in scalator, trying to avoid divisions by zero.
    
    ER = |((real + scalator) - (restored + scalator)) / (real + scalator)|
    """
    relerror = lambda y0, y1: abs((float(y0) - float(y1)) / (float(y0) + scalator))

    if matches == None:
        return [relerror(y0, y1) for (y0, y1) in zip(realy, restoredy)]
    else:
        return [relerror(y0, y1) for (y0, y1, match) in zip(realy, restoredy, matches) if not match]

def study(realy, restoredy, errormethod=abserrors, matches=None, scalator=0):
    """
    Studies the error of restoredy compared to realy via mean, median,
    standard deviation, min error and max error.
    """
    if scalator == 0:
        errors = errormethod(realy, restoredy, matches=matches)
    else:
        errors = errormethod(realy, restoredy, matches=matches, scalator=scalator) # compatibility issues

    print('Min: ', min(errors))
    print('Max: ', max(errors))
    print('Mean: ', np.mean(errors))
    print('Median: ', np.median(errors))
    print('Standard deviation: ', np.std(errors))
