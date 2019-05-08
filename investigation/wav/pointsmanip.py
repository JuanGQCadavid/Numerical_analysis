import random

# Percent is not a percent. It's a value between 0 and 1

def cut(x, y, percent):
    """
    Returns <x> and <y> without a random <percent> number of points.
    * Bug: If it cuts one of the first three points it can become a problem as
    they're used for recovering the delta time.
    """
    result = [(i, j) for i, j in zip(x[2:], y[2:]) if random.random() >= percent]
    return [i for i, j in result], [j for i, j in result]

def noisy(y, percent):
    """
    Returns <y> with a noisy random <percent> number of points.
    Noisiness means the value which was y0 becomes a value between [0, 2 * y0]
    * Maybe it's not a good function (it's a completely random criteria).
    * I've read that the gaussian distribution is a good way to add noise to a signal.
    It'd great to try using it instead of this crappy method.
    """
    newy = y.copy()

    for i in range(len(newy)):
        if random.random() < percent:
            noisepercent = -1 + 2 * random.random() # [-1, 1]
            newy[i] *= (1 + noisepercent)

    return newy

def zerofilled(y, percent):
    """Makes a <percent> of the values 0. It's a trivial function."""
    return [i if random.random() >= percent else 0 for i in y]

def inverted(y, percent):
    """Makes <percent> of the values become: y -> -y. Another trivial one."""
    return [i if random.random() >= percent else -i for i in y]

def repeated(y, percent):
    """
    <percent> of the points become: y[n] = y[n - 1].
    Why? Maybe it can work somehow.
    """
    newy = y.copy()

    for i in range(1, len(newy)):
        if random.random() < percent:
            newy[i] = newy[i - 1]

    return newy
