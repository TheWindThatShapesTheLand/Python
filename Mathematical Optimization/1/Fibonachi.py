import time
import math


def fibonacci_number(j):
    return int((((1 + 5 ** 0.5) / 2) ** j - ((1 - 5 ** 0.5) / 2) ** j) / 5 ** 0.5)


def fibonacci_method(a, b):

    eps = 10 ** -8
    n = math.floor(math.log(eps / ((b - a) * 5 ** 0.5), 2 / (5 ** 0.5 + 1)) - 1)

    for i in range(1, n + 1):
        x1 = a + (b - a) * fibonacci_number(n - i) / fibonacci_number(n - i + 2)
        x2 = a + (b - a) * fibonacci_number(n - i + 1) / fibonacci_number(n - i + 2)

        if i != n - 1:
            if math.exp(math.sin(math.cos(x1))) <= math.exp(math.sin(math.cos(x2))):
                b = x2
            else:
                a = x1
        elif i == n - 1:
            if math.exp(math.sin(math.cos(x1))) <= math.exp(math.sin(math.cos(x1 + eps))):
                b = x1 + eps
            else:
                a = x1

    print(n)
    return (a + b) / 2


A = float(-5)
B = float(-2.5)

t0 = time.time()

X = fibonacci_method(A, B)

print(X, math.exp(math.sin(math.cos(X))))
print(time.time() - t0)

# fib: X -> -3.1415926588811107, Y -> 0.43107595064559234,  n -> 40
# gr: X -> -3.1415926635164486, Y -> 0.43107595064559234, n-> 41
# dich: X -> -3.1415557863761903, Y-> 0.4310759508038779 n-> 14
# wolf: X -> -3.141592650443681, Y -> 0.43107595064559234
