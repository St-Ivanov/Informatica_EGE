with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\Поляков\6723.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]


k = 0
for stroka in sp:
    povt = [i for i in stroka if stroka.count(i) == 3]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        if sum(nepovt) / 4 <= povt[0]:
            k += 1
print(k)