import random
import numpy as np

def noiseadd(y, percent):
    """
    Returns <y> with a noisy random <percent> number of points.
    Noisiness means the value which was y0 becomes a value between [0, 2 * y0]
    * Maybe it's not a good function (it's a completely random criteria).
    * I've read that the gaussian distribution is a good way to add noise to a signal.
    It'd great to try using it instead of this crappy method.
    """
    for i in range(len(y)):
        if random.random() < percent:
            y[i] *= random.uniform(0, 2)

def zerofill(y, percent):
    """Makes a <percent> of the values 0. It's a trivial function."""
    for i in range(len(y)):
        if random.random() < percent:
            y[i] = 0

def invert(y, percent):
    """Makes <percent> of the values become: y -> -y. Another trivial one."""
    for i in range(len(y)):
        if random.random() < percent:
            y[i] = -y[i]

def repeat(y, percent):
    """
    <percent> of the points become: y[n] = y[n - 1].
    Why? Maybe it can work somehow.
    """
    for i in range(1, len(y)):
        if random.random() < percent:
            y[i] = y[i - 1]
