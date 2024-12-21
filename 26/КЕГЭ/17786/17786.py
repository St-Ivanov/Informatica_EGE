with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\17786\17786.txt') as f:
    N, M = [int(i) for i in f.readline().split()]
    sp = [int(i) for i in f.readlines()]
spisok_arb = [i for i in sp if i >= 7000 and i <= 12000]
spisok_arb.sort(reverse=True)
sm = 0
k = 0
for i in range(len(spisok_arb)):
    if sm + spisok_arb[i] <= M * 1000:
        sm += spisok_arb[i]
        k += 1
        last = spisok_arb[i]
print(k, last)