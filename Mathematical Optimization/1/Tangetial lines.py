import time
import math


def tang_line(a, b):

    eps = 10 ** -8

    while True:

        fb_p = 2 * b - 1 / (1 + b)
        fa_p = 2 * a - 1 / (1 + a)
        fa = a ** 2 - math.log(a + 1)
        fb = b ** 2 - math.log(b + 1)

        c = (b * fb_p - a * fa_p + fa - fb) / (fb_p - fa_p)

        fc_p = 2 * c - 1 / (1 + c)

        if fb_p * fa_p < 0:
            if fc_p >= 0:
                b = c
            else:
                a = c
        elif (fa_p > 0 and fb_p > 0) or (fa_p == 0):
            c = a
            break
        elif (fa_p < 0 and fb_p < 0) or (fb_p == 0):
            c = b
            break

        if abs(fc_p) <= eps:
            break

    return c


A = float(0)
B = float(2)

t0 = time.time()

X = tang_line(A, B)

print(X, X ** 2 - math.log(X + 1))
print(time.time() - t0)
