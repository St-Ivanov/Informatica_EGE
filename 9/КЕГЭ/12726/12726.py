with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\12726\12726.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
last = 0
for stroka in stroki:
    k += 1
    povt = [i for i in stroka if stroka.count(i) == 3]
    nepovt = [i for i in stroka if stroka.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        ch = [i for i in stroka if i % 2 == 0]
        nch = [i for i in stroka if i % 2 == 1]
        if len(ch) > len(nch):
            last = k
print(last)
 