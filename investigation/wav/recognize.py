def kevin(y, maxdelta):
    matches = [True] * len(y)
    laststable = y[0]

    for i in range(1, len(y)):
        delta = abs(float(laststable) - float(y[i]))

        if delta > maxdelta:
            matches[i] = False
        else:
            laststable = y[i]

    return matches
