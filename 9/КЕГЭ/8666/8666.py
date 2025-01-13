with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\8666\8666.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    if (len(set(stroka)) == 6) ^ (max(stroka) > sum(stroka) - max(stroka)):
        k += 1
print(k)