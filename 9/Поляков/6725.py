with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\Поляков\6725.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]


k = 0
for stroka in sp:
    if len(set(stroka)) == 4:
        stroka.sort()
        if (stroka[4] + stroka[0]) ** 2 < stroka[1] ** 2 + stroka[2] ** 2 + stroka[3] ** 2:
            k += 1
print(k)