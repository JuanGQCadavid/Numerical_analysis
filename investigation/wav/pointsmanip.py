import random

def cut(x, y, percent):
    result = [(i, j) for i, j in zip(x, y) if random.random() >= percent]
    return [i for i, j in result], [j for i, j in result]

def noisy(y, percent):
    newy = y.copy()

    for i in range(len(newy)):
        if random.random() < percent:
            noisepercent = -1 + 2 * random.random()
            newy[i] *= (1 + noisepercent)

    return newy
