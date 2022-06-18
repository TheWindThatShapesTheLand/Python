import math

eps = 10 ** -4


def golden_ratio(a, b):

    while abs(b - a) >= eps:
        x2 = a + (5 ** 0.5 - 1) * (b - a) / 2
        x1 = a + b - x2

        if math.sin(2 * x1) * math.cos(x1) - x1 <= math.sin(2 * x2) * math.cos(x2) - x2:
            b = x2
            x = x1
        else:
            a = x1
            x = x2

    return x


def tang_line(a, b):

    while True:

        fb_p = - 1 + 2 * math.cos(b) * math.cos(2 * b) - math.sin(b) * math.sin(2 * b)
        fa_p = - 1 + 2 * math.cos(a) * math.cos(2 * a) - math.sin(a) * math.sin(2 * a)
        fa = math.sin(2 * a) * math.cos(a) - a
        fb = math.sin(2 * b) * math.cos(b) - b

        c = (b * fb_p - a * fa_p + fa - fb) / (fb_p - fa_p)

        fc_p = - 1 + 2 * math.cos(c) * math.cos(2 * c) - math.sin(c) * math.sin(2 * c)

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
            if math.sin(2 * x1) * math.cos(x1) - x1 <= math.sin(2 * x2) * math.cos(x2) - x2:
                b = x2
            else:
                a = x1
        elif i == n - 1:
            if math.sin(2 * x1) * math.cos(x1) - x1 <= math.sin(2 * (x1 + eps)) * math.cos(x1 + eps) - (x1 + eps):
                b = x1 + eps
            else:
                a = x1

    return (a + b) / 2


def broken_line(a, b):

    eps = 10 ** -3
    L = float(2.26)

    x0 = ((math.sin(2 * a) * math.cos(a) - a) - (math.sin(2 * b) * math.cos(b) - b) + L * (a + b)) / (2 * L)
    p0 = ((math.sin(2 * a) * math.cos(a) - a) + (math.sin(2 * b) * math.cos(b) - b) + L * (a - b)) / 2

    delta_n = math.sin(2 * x0) * math.cos(x0) - x0 - p0

    points = []

    while delta_n >= eps:
        delta = delta_n / (2 * L)
        x1 = x0 - delta
        x2 = x0 + delta
        p12 = (math.sin(2 * x0) * math.cos(x0) - x0 + p0) / 2
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
        delta_n = math.sin(2 * x0) * math.cos(x0) - x0 - p0

    return x0


def newton(x):

    while abs(- 1 + 2 * math.cos(x) * math.cos(2 * x) - math.sin(x) * math.sin(2 * x)) > eps:
        x = x - (- 1 + 2 * math.cos(x) * math.cos(2 * x) - math.sin(x) * math.sin(2 * x)
                 / (- 4 * math.cos(2 * x) * math.sin(x) - 5 * math.cos(x) * math.sin(2 * x)))

    return x

def dichotomy(a, b):

    delta = 10 ** -5
    n = 0

    while ((b - a - delta) / (2 ** n + 1) + delta / 2) >= eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2

        if math.sin(2 * x1) * math.cos(x1) - x1 <= math.sin(2 * x2) * math.cos(x2) - x2:
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
    A = float(1.2)
    B = float(2)
    X = golden_ratio(A, B)
elif method == 2:
    A = float(1.2)
    B = float(2)
    X = tang_line(A, B)
elif method == 3:
    A = float(1.2)
    B = float(2)
    X = fibonacci_method(A, B)
elif method == 4:
    A = float(1)
    B = float(4.5)
    X = broken_line(A, B)
elif method == 5:
    A = float(1.2)
    B = float(2)
    X0 = golden_ratio(A, B)
    X = newton(X0)
else:
    A = float(1.2)
    B = float(2)

    X = dichotomy(A, B)
print(X, math.sin(2 * X) * math.cos(X) - X)

# gr: X -> 1.8593408916110463, Y -> -1.7040902107427938
# tan: X -> 1.8593352889068413, Y -> -1.704090210595819
# fib: X -> 1.859349593495935, Y -> -1.7040902108193705
# bl: X -> 4.022362331146197, Y -> -4.647375223817146
# newton: X -> 1.8593408916110463, Y -> -1.7040902107427938
# dich: X -> 1.8554651953125, Y -> -1.704071731441469
# wolf: X -> 1.8593488952846022, Y -> -1.7040902108200364
