with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\14251\14251.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    povt = [i for i in stroka if stroka.count(i) == 2]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    if len(povt) == 4 and len(nepovt) == 3:
        nch = [i for i in stroka if i % 2 == 1]
        if sum(povt) <= sum(nch):
            print(sum(stroka))
            break