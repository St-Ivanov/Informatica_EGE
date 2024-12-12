with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\18174\18174.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    if len(set(stroka)) == 5:
        otr = abs(sum([i for i in stroka if i < 0]))
        pol = sum([i for i in stroka if i > 0])
        if otr > pol:
            k += 1
print(k)