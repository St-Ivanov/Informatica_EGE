from math import dist
with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\27A.txt') as f:
    sp = [[float(j) for j in i.replace(',', '.').split()] for i in f.readlines()]
clast = [[] for i in range(2)]
for x, y in sp:
    tochka = [x, y]
    if y > 15:
        clast[0].append(tochka)
    else:
        clast[1].append(tochka)
def centroid(cl):
    mn = 10 ** 100
    tochka_centroid = 0
    for i in cl:
        sm = 0
        for j in cl:
            sm += dist(i, j)
        if mn > sm:
            mn = sm
            tochka_centroid = i
    return tochka_centroid
x1 = 0
y1 = 0
sm = 0
for cl in clast:
    sm += len(cl)
    x, y = centroid(cl)
    x1 += x
    y1 += y
print(abs(x1 * 10000 // len(clast)), abs(y1 * 10000 // len(clast)))