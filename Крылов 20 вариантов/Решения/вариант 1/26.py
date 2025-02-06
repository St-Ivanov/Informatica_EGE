with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\26var01.txt') as f:
    N, M, K = [int(i) for i in f.readline().split()]
    pole = [[] for i in range(K + 1)]
    for i in f.readlines():
        i = [int(j) for j in i.split()]
        pole[i[1]].append(i[0])
mx = 0
gr = 0
for i in range(len(pole) - 1):
    num1, num2 = pole[i], pole[i + 1]
    mn = min(num1 + num2) - 1
    if mn > mx:
        mx = mn
        gr = i
print(mx, gr)