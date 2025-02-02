with open(r'C:\Users\si655\OneDrive\Документы\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\26var01.txt') as f:
    N, M, K = [int(i) for i in f.readline().split()]
    mat = [[0] * (M + 1) for i in range(K + 1)]
    slovar = {}
    for i in f.readlines():
        i = [int(j) for j in i.split()]
        if i[1] in slovar.keys():
            slovar[i[1]].append(i[0])
        else:
            slovar[i[1]] = [i[0]]
keys = sorted([i for i in slovar.keys()], reverse=True)
mx = 0
gr = 0
dr = 0
for key in keys:
    if mx < max(slovar[key]):
        mx = max(slovar[key])
        gr = max(slovar[key]) + 1
        dr = key
print(gr, dr)