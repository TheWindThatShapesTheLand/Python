import math
import time


n = 3
x0 = []
t0 = time.time()

for t in range(n):
    x0 += [-1]


def func(x):
    #return x[0] ** 3 + 2 * x[1] ** 2 - 3 * x[0] - 4 * x[1]
     return x[0] + 2 * x[1] + 4 * (1 + x[0] ** 2 + x[1] ** 2) ** 0.5
    #return x[1] ** 2 + x[2] ** 2 + math.exp(x[0] ** 2 + x[1] ** 2 + x[2] ** 2) + x[0] - x[1]


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
