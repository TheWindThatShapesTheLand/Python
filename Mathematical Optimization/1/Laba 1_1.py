import math

eps = 10 ** -5


def golden_ratio(a, b):

    while abs(b - a) >= eps:
        x2 = a + (5 ** 0.5 - 1) * (b - a) / 2
        x1 = a + b - x2

        if x1 ** 5 - 5 * x1 ** 3 + 10 * x1 ** 2 - 5 * x1 <= x2 ** 5 - 5 * x2 ** 3 + 10 * x2 ** 2 - 5 * x2:
            b = x2
            x = x1
        else:
            a = x1
            x = x2

    return x


def tang_line(a, b):

    while True:

        fb_p = - 5 + 20 * b - 15 * b ** 2 + 5 * b ** 4
        fa_p = - 5 + 20 * a - 15 * a ** 2 + 5 * a ** 4
        fa = a ** 5 - 5 * a ** 3 + 10 * a ** 2 - 5 * a
        fb = b ** 5 - 5 * b ** 3 + 10 * b ** 2 - 5 * b

        c = (b * fb_p - a * fa_p + fa - fb) / (fb_p - fa_p)

        fc_p = - 5 + 20 * c - 15 * c ** 2 + 5 * c ** 4

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


def fibonacci_number(j):
    return int((((1 + 5 ** 0.5) / 2) ** j - ((1 - 5 ** 0.5) / 2) ** j) / 5 ** 0.5)


def fibonacci_method(a, b):

    n = math.floor(math.log(eps / ((b - a) * 5 ** 0.5), 2 / (5 ** 0.5 + 1)) - 1)

    for i in range(1, n + 1):
        x1 = a + (b - a) * fibonacci_number(n - i) / fibonacci_number(n - i + 2)
        x2 = a + (b - a) * fibonacci_number(n - i + 1) / fibonacci_number(n - i + 2)

        if i != n - 1:
            if x1 ** 5 - 5 * x1 ** 3 + 10 * x1 ** 2 - 5 * x1 <= x2 ** 5 - 5 * x2 ** 3 + 10 * x2 ** 2 - 5 * x2:
                b = x2
            else:
                a = x1
        elif i == n - 1:
            if x1 ** 5 - 5 * x1 ** 3 + 10 * x1 ** 2 - 5 * x1 <= (x1 + eps) ** 5 - 5 * (x1 + eps) ** 3 + 10 * (x1 + eps) ** 2 - 5 * (x1 + eps):
                b = x1 + eps
            else:
                a = x1

    return (a + b) / 2


def broken_line(a, b):

    eps = 10 ** -3
    L = float(183)

    x0 = ((a ** 5 - 5 * a ** 3 + 10 * a ** 2 - 5 * a) - (b ** 5 - 5 * b ** 3 + 10 * b ** 2 - 5 * b) + L * (a + b)) / (2 * L)
    p0 = ((a ** 5 - 5 * a ** 3 + 10 * a ** 2 - 5 * a) + (b ** 5 - 5 * b ** 3 + 10 * b ** 2 - 5 * b) + L * (a - b)) / 2

    delta_n = x0 ** 5 - 5 * x0 ** 3 + 10 * x0 ** 2 - 5 * x0 - p0

    points = []

    while delta_n >= eps:
        delta = delta_n / (2 * L)
        x1 = x0 - delta
        x2 = x0 + delta
        p12 = (x0 ** 5 - 5 * x0 ** 3 + 10 * x0 ** 2 - 5 * x0 + p0) / 2
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
        delta_n = x0 ** 5 - 5 * x0 ** 3 + 10 * x0 ** 2 - 5 * x0 - p0

    return x0


def newton(x):

    while abs(- 5 + 20 * x - 15 * x ** 2 + 5 * x ** 4) > eps:
        x = x - ((- 5 + 20 * x - 15 * x ** 2 + 5 * x ** 4) / (20 - 30 * x + 20 * x ** 3))

    return x

def dichotomy(a, b):

    delta = 10 ** -6
    n = 0

    while ((b - a - delta) / (2 ** n + 1) + delta / 2) >= eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2

        if x1 ** 5 - 5 * x1 ** 3 + 10 * x1 ** 2 - 5 * x1 <= x2 ** 5 - 5 * x2 ** 3 + 10 * x2 ** 2 - 5 * x2:
            b = x2
        else:
            a = x1
        n += 1

    return (a + b) / 2


print("Enter your method: 1 -> Gr, 2 -> Tang, 3 -> Fib, 4 -> BL, 5 -> Newton, 6 ->  Dich")

try:
    method = int(input())
    if method < 1 or method > 6:
        method = int("Meow")
except ValueError:
    print("Wrong input!")
    quit()

if method == 1:
    A = float(-1)
    B = float(3)
    X = golden_ratio(A, B)
elif method == 2:
    A = float(-1)
    B = float(3)
    X = tang_line(A, B)
elif method == 3:
    A = float(-1)
    B = float(3)
    X = fibonacci_method(A, B)
elif method == 4:
    A = float(-2)
    B = float(3)
    X = broken_line(A, B)
elif method == 5:
    A = float(-1)
    B = float(3)
    X0 = golden_ratio(A, B)
    X = newton(X0)
else:
    A = float(-1)
    B = float(3)

    X = dichotomy(A, B)
print(X, X ** 5 - 5 * X ** 3 + 10 * X ** 2 - 5 * X)


# gr: X -> 0.3276244280818591, Y -> -0.7368021616634159
# tang: X -> 0.32762206773321, Y -> -0.7368021617016997
# fib: X -> 0.32761795235218427, Y -> -0.7368021616235436
# Bl: X -> 0.3276143438658115, Y -> -0.7368021614034663
# newton: X -> 0.32762175640447366, Y -> -0.7368021617022267
# dich: X -> 0.32617204345703127, Y -> -0.736790722271113
# wolf: X -> 0.32762176344830396, Y -> -0.7368021617022263
