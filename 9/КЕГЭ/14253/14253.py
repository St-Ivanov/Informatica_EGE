with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\14253\14253.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    povt = [i for i in stroka if stroka.count(i) == 2]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    sr = sum(stroka) / len(stroka)
    if (len(povt) == 6 and len(nepovt) == 1) or (sr ** 0.5 == int(sr ** 0.5)):
        k += 1
print(k)
