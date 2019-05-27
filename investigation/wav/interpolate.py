import numpy as np

class NewtonInterpolator:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

        n = len(xs)
        divdiffs = [None] * n
        for i in range(n):
            divdiffs[i] = [None] * (i + 1)
            divdiffs[i][0] = ys[i]

        for i in range(1, n):
            for j in range(i, n):
                num = divdiffs[j][i - 1] - divdiffs[j - 1][i - 1]
                den = xs[j] - xs[j - i]
                divdiffs[j][i] = num / den

        self.n = n
        self.divdiffs = divdiffs

    def evaluate(self, x):
        result = 0

        for i in reversed(range(1, self.n)):
            result = (result + self.divdiffs[i][i]) * (x - self.xs[i - 1])

        return result + self.divdiffs[0][0]

    def __call__(self, x):
        if isinstance(x, list):
            return [self.evaluate(x0) for x0 in x]
        else:
            return self.evaluate(x)
