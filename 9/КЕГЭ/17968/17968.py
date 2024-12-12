with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\17968\17968.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    if max(stroka) < sum(stroka) - max(stroka):
        ch = sum([i for i in stroka if i % 2 == 0])
        nch = sum([i for i in stroka if i % 2 == 1])
        if ch == nch:
            k += 1
print(k)
