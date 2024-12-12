from math import prod
with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\11830\11830.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    povt = [i for i in stroka if stroka.count(i) == 2]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    if len(povt) == 4 and len(nepovt) == 3:
        if prod(povt) / 2 > prod(nepovt):
            k += 1
print(k)