import time
import math


def golden_ratio(a, b):

    eps = 10 ** -8
    n = 0

    while abs(b - a) >= eps:
        x2 = a + (5 ** 0.5 - 1) * (b - a) / 2
        x1 = a + b - x2

        if math.exp(math.sin(math.cos(x1))) <= math.exp(math.sin(math.cos(x2))):
            b = x2
            x = x1
        else:
            a = x1
            x = x2
        n += 1

    print(n)
    return x


A = float(-5)
B = float(-2.5)

t0 = time.time()

X = golden_ratio(A, B)

print(X, math.exp(math.sin(math.cos(X))))
time.sleep(10**-100)
print(time.time() - t0 - 10 ** -100)
