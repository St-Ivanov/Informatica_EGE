from math import dist
with open(r'Крылов 20 вариантов\Решения\вариант 2\27A.txt') as f:
    sp = [[float(j) for j in i.replace(',', '.').split()] for i in f.readlines()]
clast = [[] for _ in range(2)]
for x, y in sp:
    i = [x, y]
    if y > 15:
        clast[0].append(i)
    else:
        clast[1].append(i)
def centroid(cl):
    mn = 10 ** 10
    id = []
    for i in cl:
        sm = 0
        for j in cl:
            sm += dist(i, j)
        if sm < mn:
            mn = sm
            id = i
    return id
x0 = 0
y0 = 0
for cl in clast:
    x, y = centroid(cl)
    x0 += x
    y0 += y
print(abs(x0 * 10000 / len(clast)), abs(y0 * 10000 / len(clast)))