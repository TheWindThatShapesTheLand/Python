import math
from scipy import integrate
temp_a = []
temp_b = []
old_x = []
old_y = []


def liner_reg():
    '''
    if i == 1:
        f = open("USA TV.txt")
    else:
        f = open("USA TV (no Ny).txt")
    '''

    x0 = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9]
    y1 = [0.94, 0.93, 0.75, 0.79, 0.4, 0.44, 0.42, 0.17, 0.23, -0.03]
    y2 = [1.03, 0.96, 0.84, 0.65, 0.64, 0.44, 0.21, 0.21, 0.46, 0.22]

    temp_xy = []
    temp_sigma = []

    n = len(x0)
    x = sum(x0) / n
    k = 0
    A = []
    B = []
    temp_y = []

    while k != 2:
        if k == 0:
            Y1 = sum(y1) / n
        else:
            Y1 = sum(y2) / n

        for j in range(n):
            if k == 0:
                temp_xy += [x0[j] * y1[j]]
            else:
                temp_xy += [x0[j] * y2[j]]

            temp_sigma += [(x0[j] - x) ** 2]

        XY = sum(temp_xy) / n
        sigma = sum(temp_sigma) / n

        b = (XY - x * Y1) / sigma
        a = Y1 - b * x
        A += [a]
        B += [b]

        k += 1
    k = 0
    a = sum(A) / 2
    b = sum(B) / 2
    print(f"a = {a}; b = {b}")

    f = open("newXY.txt", 'w')

    this_y = []
    for i in x0:
        new_y = a + b * i
        this_y += [new_y]

        f.write(str(i) + '\t' + str(new_y) + '\n')

    f.close()

    temp_rss = []
    while k != 2:
        if k == 0:
            for i in range(n):
                temp_rss += [(y1[i] - a - b * x0[i]) ** 2]
        else:
            for i in range(n):
                temp_rss += [(y2[i] - a - b * x0[i]) ** 2]

        k += 1

    k = 0
    rss = sum(temp_rss)

    sigma = (rss / 18) ** 0.5

    print(f'rss = {rss}; sigma = {sigma}')

    z0 = 8.23
    z1 = 31.5

    ss = [(rss / z0) ** 0.5, (rss / z1) ** 0.5]

    ss = sorted(ss)

    print(f'Доверительный интевал для sigma: {ss}')

    w0 = 2.101

    temp_x = []
    temp_y = []
    for i in x0:
        temp_x += [(i - x) ** 2]

    DB = sigma / sum(temp_x)

    sa = [a + w0 * DB, a - w0 * DB]
    sb = [b + w0 * DB, b - w0 * DB]

    sa = sorted(sa)
    sb = sorted(sb)

    print(f'Доверительный интевал для a:{sa}')
    print(f'Доверительный интевал для b:{sb}')
    temp_delta = []
    for i in range(n):
        temp_delta += [abs(y1[i] - this_y[i])]
        temp_delta += [abs(y2[i] - this_y[i])]

    delta = max(temp_delta)

    print(f'Максимальный остаток:{delta}', f'Оценка: {2 * sigma}')

    DB1 = sigma * (1 + (1 / n) + (((x0[8] * x - x) ** 2)/sum(temp_x))) ** 0.5
    sy = [y2[8] + w0 * DB1, y2[8] - w0 * DB1 ]

    sy = sorted(sy)
    print(f'Доверительный интевал для y(9):{sy}')


liner_reg()
