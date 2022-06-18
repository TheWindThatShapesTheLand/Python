import time
import math


def dichotomy(a, b):

    eps = 10 ** -8
    delta = 10 ** -9
    n = 0

    while ((b - a - delta) / (2 ** n + 1) + delta / 2) >= eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2

        if math.exp(math.sin(math.cos(x1))) <= math.exp(math.sin(math.cos(x2))):
            b = x2
        else:
            a = x1
        n += 1

    print(n)
    return (a + b) / 2


A = float(-5)
B = float(-2.5)

t0 = time.time()

X = dichotomy(A, B)

print(X, math.exp(math.sin(math.cos(X))))
print(time.time() - t0)
