from math import dist
with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\27\КЕГЭ\18622\A.txt') as f:
    sp = [[float(j) for j in i.replace(',', '.').split()] for i in f.readlines()]
clast = [[] for i in range(3)]
for i in sp:
    if i[1] > 6:
        clast[0].append(i)
    elif i[1] > 2:
        clast[1].append(i)
    else:
        clast[2].append(i)
def center(cl):
    rt = []
    mn = 10 ** 100
    for i in cl:
        sm = 0
        for j in cl:
            sm += dist(i, j)
        if mn > sm:
            mn = sm
            rt = i
    return rt
clast.sort(key=len)
clast = clast[:-1]
sm_x, sm_y = 0, 0
for i in clast:
    x, y = center(i)
    sm_x += x
    sm_y += y
print(sm_x * 10000 / len(clast), sm_y * 10000 / len(clast))