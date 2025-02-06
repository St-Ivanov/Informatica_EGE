with open(r'Крылов 20 вариантов\Решения\вариант 2\26var02.txt') as f:
    N, M, K = [int(i) for i in f.readline().split()]
    pole = [[] for _ in range(K + 1)]
    for i in f.readlines():
        i = [int(j) for j in i.split()]
        pole[i[1]].append(i[0])
mx = 0
gr = 0
for i in range(len(pole) - 2):
    x, y, z = pole[i], pole[i + 1], pole[i + 2]
    mn = min(x + y + z) - 1
    if mn > mx:
        mx = mn
        gr = i + 2
print(mx, gr)
