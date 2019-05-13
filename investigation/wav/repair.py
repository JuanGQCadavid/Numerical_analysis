def linearinterpolation(y, marks):
    """
    Interpolates values marked as False with the two nearest
    enclosing values marked as True. In limits it only duplicates.
    
    linearinterpolation([0, 1, -1, 2, 4, 0], [False, True, False, False, True, True])
    => [1, 1, 2, 3, 4, 0]
    """
    prev, curr = -1, 0

    while curr < len(y):
        if marks[curr]:
            if prev == -1:
                for i in range(prev + 1, curr):
                    y[i] = y[curr]
            else:
                m = (float(y[curr]) - float(y[prev])) / (curr - prev)
                for i in range(1, curr - prev):
                    y[prev + i] = m * i + y[prev]
            prev = curr
        curr += 1

    if prev != len(y) - 1 and prev != -1:
        for i in range(prev + 1, len(y)):
            y[i] = y[prev]
