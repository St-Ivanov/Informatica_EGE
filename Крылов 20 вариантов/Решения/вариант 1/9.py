with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\9.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
count = 0
for stroka in stroki:
    stroka.sort()
    if stroka[-1] < (stroka[0] + stroka[1] + stroka[2]):
        if len(set(stroka)) == 4:
            count += 1
print(count)