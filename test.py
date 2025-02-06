# from math import dist
# with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt') as f:
#     sp = [[float(j) for j in i.replace(',', '.').split()] for i in f.readlines()]
# clast = []
# eps = 0.7
# while sp:
#     clast.append([sp.pop()])
#     for el1 in clast[-1]:
#         for el2 in sp.copy():
#             if dist(el1, el2) <= eps:
#                 clast[-1].append(el2)
#                 sp.remove(el2)
# def centroid(cl):
#     mn = 10 ** 10
#     id = []
#     for i in cl:
#         sm = 0
#         for j in cl:
#             sm += dist(i, j)
#         if mn > sm:
#             mn = sm
#             id = i
#     return id
# x0 = 0
# y0 = 0
# clast = [i for i in clast if len(i) > 30]
# for cl in clast:
#     x, y = centroid(cl)
#     x0 += x
#     y0 += y
# print(x0 * 100000 / len(clast), y0 * 100000 / len(clast))

# from itertools import product
# alf = ''.join(sorted(list('ПРЕСТОЛ')))
# print(alf)
# num = 0
# k = 0
# for i in product(alf, repeat=5):
#     num += 1
#     if num % 2 == 1:
#         if i[-1] in 'ЕО':
#             if (5 - (i.count('Е') + i.count('О'))) <= 3:
#                 k += 1
# print(k)

# with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt') as f:
#     sp = [int(i) for i in f.readlines()]
# mn = min([i for i in sp if i > 0 and i % 10 == 4])
# ans = []
# for i in range(len(sp) - 2):
#     x, y, z = sp[i], sp[i + 1], sp[i + 2]
#     sm = sum([int(j) for j in str(abs(x))]) + sum([int(j) for j in str(abs(y))]) + sum([int(j) for j in str(abs(z))])
#     if sm == mn:
#         ans.append(x + y + z)
# print(len(ans), max(ans))

# from re import findall
# mx = 0
# for i in findall(r'', open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt').readline()):
#     print(i)
#     mx = max(mx, len(i))
# print(mx)

# def f(x, y, h):
#     if x + y >= 77:
#         return h % 2 == 0
#     elif h == 0:
#         return 0
#     else:
#         ans = [f(x + 3, y, h - 1), f(x * 3, y, h - 1), f(x, y + 3, h - 1), f(x, y * 3, h - 1)]
#         if h % 2 == 1:
#             return any(ans) # Ходы Вани
#         return all(ans) # Ходы Пети
# print([i for i in range(1, 65) if f(12, i, 2)]) # Задача 19
# print([i for i in range(1, 65) if f(12, i, 3) and not f(12, i, 1)]) # Задача 20
# print(len([i for i in range(1, 65) if (f(12, i, 4) or f(12, i, 2)) and not f(12, i, 2)])) # Задача 21


# with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt') as f:
#     N, K = [int(i) for i in f.readline().split()]
#     sp = [[int(i) for i in f.readline().split()] for _ in range(N)]
#     seans = [int(i) for i in f.readlines()]
# sp.sort(key=lambda x: (-x[1], x[0]))
# poshli = 0
# count = 0
# for _, _, kol in sp:
#     seans.sort()
#     for i in range(len(seans)):
#         if seans[i] >= kol:
#             seans[i] = 0
#             poshli += kol
#             count += 1
#             break
# print(count, poshli)

# from math import ceil
# import itertools
# def f(x, x0, x1):
#     p = 64 <= x <= 95
#     q = 72 <= x <= 106
#     a = x0 <= x <= x1
#     return (q and (not a)) <= ((not p) <= (not q))
# res = []
# xa = [x / 4 for x in range(60 * 4, 110 * 4)]
# for x0, x1 in itertools.combinations(xa, 2):
#     print(x0, x1)
#     if all(f(x, x0, x1) for x in xa):
#         res.append(x1 - x0)
# print(ceil(min(res)))


with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt') as f:
    N = f.readline()
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
sp.sort(key=lambda x: (x[1], x[0]))
time = [True] * 1440
konf = []
for start, end in sp:
    if all(time[start:end]):
        for i in range(start, end):
            time[i] = False
        konf.append([start, end])
mx = 0
ans1 = len(konf)
sp123123 = [i for i in sp if i[0] >= konf[-2][1]]
for i in sp123123:
    if mx < i[1] - i[0]:
        mx = i[1] - i[0]
        ans2 = i
print(ans1, ans2[1] - konf[0][0])