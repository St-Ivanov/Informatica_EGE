with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\Поляков\6819.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]


k = 0
for stroka in sp:
    if len(set(stroka)) == 3:
        stroka.sort()
        if stroka[2] + stroka[3] > (stroka[0] + stroka[1]) * 2:
            if max(stroka) % min(stroka) != 0:
                k += 1
print(k)