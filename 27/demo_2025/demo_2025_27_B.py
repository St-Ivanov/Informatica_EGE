from math import sqrt


def evcld(d1, d2):
    return sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]))


min__ = 10**10
with open('27/demo_2025_27_B.txt') as f:
    f.readline()
    sp = [list(map(float, i.replace(',', '.').split())) for i in f.readlines()]
