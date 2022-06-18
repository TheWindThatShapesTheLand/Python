import time
import math


def broken_line(a, b):

    x0 = ((math.exp(math.sin(math.cos(a)))) - (math.exp(math.sin(math.cos(b)))) + L * (a + b)) / (2 * L)
    p0 = ((math.exp(math.sin(math.cos(a)))) + (math.exp(math.sin(math.cos(b)))) + L * (a - b)) / 2

    delta_n = (math.exp(math.sin(math.cos(x0)))) - p0
    eps = 10 ** -6

    points = []

    while delta_n >= eps:
        delta = delta_n / (2 * L)
        x1 = x0 - delta
        x2 = x0 + delta
        p12 = ((math.exp(math.sin(math.cos(x0)))) + p0) / 2
        points += [[x1, p12], [x2, p12]]
        min_p = points[0][1]
        min_point = points[0]

        for i in range(1, len(points)):
            if points[i][1] < min_p:
                min_p = points[i][1]
                min_point = points[i]

        points.remove(min_point)
        x0 = min_point[0]
        p0 = min_point[1]
        delta_n = (math.exp(math.sin(math.cos(x0)))) - p0

    return x0


A = float(-5)
B = float(-2.5)
L = float(1.32)

t0 = time.time()

X = broken_line(A, B)

print(X, (math.exp(math.sin(math.cos(X)))))
print(time.time() - t0)

