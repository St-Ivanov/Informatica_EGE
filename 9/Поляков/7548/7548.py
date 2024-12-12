with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\Поляков\7548.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]


k = 0
for stroka in sp:
    if len(set(stroka)) == 4:
        stroka.sort()
        if stroka[0] + stroka[3] > stroka[1] + stroka[2]:
            k += 1
print(k)