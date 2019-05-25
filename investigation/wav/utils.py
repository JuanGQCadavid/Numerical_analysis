def tovalidxy(y, marks):
    """
    Returns two arrays: x and y, where only points marked as True
    are considered.
    """
    n = marks.count(True)

    validx = [None] * n
    validy = [None] * n

    cnt = 0
    for i in range(len(y)):
        if marks[i]:
            validx[cnt] = i
            validy[cnt] = y[i]
            cnt += 1

    return validx, validy

def repair(y, marks, fn):
    """
    Replaces the value of the <y> if the value of <marks> is
    false in that index. y[i] = fn[i]
    """
    for i in range(len(y)):
        if not marks[i]:
            y[i] = fn(i)
