with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\test.txt') as f:
    N = f.readline()
    slovar = {}
    for i in f.readlines():
        i = [int(j) for j in i.split()]
        if i[0] in slovar.keys():
            slovar[i[0]].append(i[1])
        else:
            slovar[i[0]] = [i[1]]
ans = []
for key in slovar:
    sp = list(set(slovar[key]))
    sp.sort()
    k = 1
    for i in range(len(sp) - 2):
        if sp[i] == sp[i + 1] - 2 and sp[i] == sp[i + 2] - 4:
            k += 1
        else:
            if k == 2:
                ans.append([key, sp[i] - 1])
            k = 1
    if k == 2:
        ans.append([key, sp[i] - 1])
ans.sort(key=lambda x: (x[0], -x[1]))
print(ans[-1])