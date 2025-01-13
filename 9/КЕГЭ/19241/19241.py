with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\19241\19241.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    k += 1
    povt = [i for i in stroka if stroka.count(i) == 3]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    if len(povt) == 6 and len(nepovt) == 1:
        if sum(povt) / 6 < nepovt[0]:
            last = k
print(last)