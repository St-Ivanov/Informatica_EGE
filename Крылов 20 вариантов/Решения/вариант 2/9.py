with open(r'Крылов 20 вариантов\Решения\вариант 2\9.txt') as f:
    stroki = [[int(j) for j in i.split(';')] for i in f.readlines()]
k = 0
for stroka in stroki:
    stroka.sort()
    if len(set(stroka)) == 4 and (stroka[0] + stroka[1] + stroka[2]) < stroka[3]:
        k += 1
print(k)