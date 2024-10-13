with open('9/Авторские/2/1.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
kol = 0
for stroka in sp:
    if stroka.count(min(stroka)) == 1:
        if len(set(stroka)) < 6:
            if max(stroka) > ((sum(stroka) - max(stroka)) / 5) * 3:
                kol += 1
print(kol)