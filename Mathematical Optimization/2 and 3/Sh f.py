import math
import os
import time

k = 10
n = 2
t0 = time.time()
x0 = [-0.04375, 0.09375]


def func(x):
    return x[0]**2 + x[1] ** 2 - 10 * x[0] - 15 * x[1] + k * (max(g1(x), 0)) ** k +  k *(max(g2(x), 0)) ** 2


def g1(x):
    return 5 * x[0] + 13 * x[1] - 51


def g2(x):
    return 15 * x[0] + 7 * x[1] - 107


def hj(x):

    delta = 10 ** -3
    eps = 10 ** -4
    lam = 10 ** -2
    alpha = 1.2

    y = x.copy()

    while True:
        for i in range(len(x)):
            if func([y[j] + delta if j == i else y[j] for j in range(len(y))]) < func(y):
                y[i] += delta

            elif func([y[j] - delta if j == i else y[j] for j in range(len(y))]) < func(y):
                y[i] -= delta

            if func(y) < func(x):

                temp = x
                x = y.copy()
                y = [x[i] + lam * (x[i] - temp[i]) for i in range(len(x))]

            else:
                if delta > eps:
                    return x
                else:
                    delta /= alpha
                    y = x.copy()


X = hj(x0)
print(X, func(X), time.time() - t0)








