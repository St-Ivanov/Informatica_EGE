with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\9\КЕГЭ\6925\6925.txt') as f:
    stroki = [[int(j) for j in i.split()] for i in f.readlines()]
k = 0
for stroka in stroki:
    ch = [i for i in stroka if i % 2 == 0]
    nch = [i for i in stroka if i % 2 == 1]
    if len(ch) == 0:
        sr1 = 0
    else:
        sr1 = sum(ch) / len(ch)
    if len(nch) == 0:
        sr2 = 0
    else:
        sr2 = sum(nch) / len(nch)
    if (len(set(stroka)) == 5) ^ (abs(sr1 - sr2) > 50):
        k += 1
print(k)