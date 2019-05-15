import matplotlib.pyplot as plt
def damage_recognition(n, y, damage_parameter):
    x_to_interpolate = [True] * n
    print(n)
    print(len(y))
    i = 1
    last_stable = y[0]
    while i < n-1:
        delta = abs(last_stable - y[i])
        if delta > damage_parameter:
            x_to_interpolate[i] = False
        else:
            last_stable = y[i]
        i = i + 1
    return x_to_interpolate
## Testing
#x = [0,1,2,3,4,5,6,7,8,9]
#y = [0.1,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2]
#damaged_y = y.copy()
#damaged_y[1] = -0.4
#damaged_y[2] = 0.9
#damaged_y[5] = -0.4
#damaged_y[6] = -0.4
#
#plt.plot(x,y)
#plt.plot(x,damaged_y)
#
#x_indixes = damage_recognition(len(x),damaged_y,0.2)
#for i in range(len(x_indixes)):
#    print(str(x[i]) + " : " + str(x_indixes[i]))

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
