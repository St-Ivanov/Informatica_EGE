with open('9/Авторские/3/1.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
kol = 0
for i in sp:
    povt = 0
    for x in i:
        if i.count(x) == 3:
            povt = x
    if len(set(i)) == 5 and povt != 0:
        if (sum(i) - povt * 3) / 3 <= povt:
            kol += 1
print(kol)