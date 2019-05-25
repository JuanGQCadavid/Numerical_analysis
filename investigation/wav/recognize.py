def cheat(y0, y1):
    """
    Returns an array of True if y0[i] == y1[i], False otherwise.
    """
    return [i == j for (i, j) in zip(y0, y1)]

def kevin(y, maxdelta):
    """
    Recognizes via a method defined by Kevin.
    """
    matches = [True] * len(y)
    laststable = y[0]

    for i in range(1, len(y)):
        delta = abs(float(laststable) - float(y[i]))

        if delta > maxdelta:
            matches[i] = False
        else:
            laststable = y[i]

    return matches
