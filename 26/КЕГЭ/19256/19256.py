with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\19256\19256.txt') as f:
    N = f.readline()
    slovar = {}
    for i in f.readlines():
        i = [int(j) for j in i.split()]
        if i[0] in slovar.keys():
            slovar[i[0]].append(i[1])
            slovar[i[0]].sort()
        else:
            slovar[i[0]] = [i[1]]
mx = 0
for key in slovar.keys():
    uch = slovar[key]
    k = 1
    for i in range(len(uch) - 1):
        if uch[i] == uch[i + 1] - 1:
            k += 1
            mx = max(mx, k)
        else:
            k = 1
ans = []
for key in slovar.keys():
    uch = slovar[key]
    k = 1
    for i in range(len(uch) - 1):
        if uch[i] == uch[i + 1] - 1:
            k += 1
            if k == mx:
                ans.append(key)
        else:
            k = 1
print(min(ans), mx)