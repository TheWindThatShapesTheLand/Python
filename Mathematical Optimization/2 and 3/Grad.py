import math
import time


n = 3
x0 = []
t0 = time.time()

for t in range(n):
    x0 += [-1]


def func(x):
    #return x[0] ** 3 + 2 * x[1] ** 2 - 3 * x[0] - 4 * x[1]
    #return x[0] + 2 * x[1] + 4 * (1 + x[0] ** 2 + x[1] ** 2) ** 0.5
    return x[1] ** 2 + x[2] ** 2 + math.exp(x[0] ** 2 + x[1] ** 2 + x[2] ** 2) + x[0] - x[1]


def der(x, j):
    delta = 10 ** -3
    y = x.copy()
    y[j] = y[j] + delta

    return (func(y) - func(x)) / delta


def grad(x):
    d = 0
    for k in range(len(x)):
        d += (der(x, k)) ** 2

    d **= 0.5

    return d


def grad_method(x):
    h = 10 ** -4
    eps = 10 ** -5
    X = []

    for q in range(len(x)):
        X += [q]

    while True:

        for i in range(len(x)):
            X[i] = x[i] - h * der(x, i)


        if func(X) < func(x):
            h /= 2

        x = X

        if grad(X) < eps:
            return X


f = grad_method(x0)
print(f, func(f), time.time() - t0)
