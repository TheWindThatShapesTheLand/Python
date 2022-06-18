import time
import math


def golden_ratio(a, b):

    eps = 10 ** -8

    while abs(b - a) >= eps:
        x2 = a + (5 ** 0.5 - 1) * (b - a) / 2
        x1 = a + b - x2

        if x1 ** 2 - math.log(x1 + 1) <= x2 ** 2 - math.log(x2 + 1):
            b = x2
            x = x1
        else:
            a = x1
            x = x2

    return x


def newton(x):

    eps = 10 ** -8

    while abs(2 * x - 1 / (1 + x)) > eps:
        x = x - ((2 * x - 1 / (1 + x)) / (2 + 1 / (1 + x) ** 2))

    return x


A = float(0)
B = float(2)

X0 = golden_ratio(A, B)
t0 = time.time()
X = newton(X0)

print(X0, X0 ** 2 - math.log(X0 + 1))
print(X, X ** 2 - math.log(X + 1))
print(time.time() - t0)


