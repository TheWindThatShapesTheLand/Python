import math
f = open("C:\\Users\\Коптутер\\Desktop\\Универ\\Теорвер\\steel\\Steel.txt", 'r')

x = []
y = []
k = 0

for i in f.readlines():
    if 0 <= k < 2:
        x += [int(i[:1])]
        y += [1 / float(i[2:6])]
    elif 2 <= k < 10:
        x += [int(i[:1])]
        y += [1 / float(i[2:7])]
    else:
        x += [int(i[:2])]
        y += [1 / float(i[3:8])]

    k += 1

f.close()
g = open("LogSteel.txt", 'w')
n = len(x)
for i in range(n):
    g.write(str(x[i]) + '\t' + str(y[i]) + '\n')
g.close()


temp_x2 = []
temp_x3 = []
temp_x4 = []
temp_xy1 = []
temp_xy2 = []

for i in x:
    temp_x2 += [i ** 2]
    temp_x3 += [i ** 3]
    temp_x4 += [i ** 4]

for i in range(n):
    temp_xy1 += [y[i] * x[i]]
    temp_xy2 += [y[i] * x[i] ** 2]

x1 = sum(x) / n
x2 = sum(temp_x2) / n
x3 = sum(temp_x3) / n
x4 = sum(temp_x4) / n
y1 = sum(y) / n
y2 = sum(temp_xy1) / n
y3 = sum(temp_xy2) / n

print(1, x1, x2, y1)
print(x1, x2, x3, y2)
print(x2, x3, x4, y3)

new_x = [0.0999952, -0.00319196, 2.99937e-05]


g = open("LogParab.txt", 'w')

for i in range(n):
    new_y = new_x[0] + new_x[1] * x[i] + new_x[2] * x[i] ** 2
    g.write(str(x[i]) + '\t' + str(new_y) + '\n')

g.close()