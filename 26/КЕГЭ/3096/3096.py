with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\3096\3096.txt') as f:
    N, st, en = [int(i) for i in f.readline().split()]
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
next_smotr = st
count = 0
while next_smotr <= en:
    next_smotr = max([i[1] for i in sp if i[0] < next_smotr])
    if count == 0:
        ans = next_smotr - st
    count += 1
print(count, ans)
    