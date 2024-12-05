with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\Авторские\12\1.txt') as f:
    N, M, K = [int(j) for j in f.readline().split()]
    sp = [[int(j) for j in i.split()] for i in f.readlines()]

for i in range(len(sp)):
    sp[i][0] -= 1
    sp[i][1] -= 1

kol = 0
mx = 0
mesta = [[1] * M for i in range(N)]
for row, num in sp:
    if num == 0:
        mesta[row][num] = 0
        mesta[row][num + 1] = 0
    elif num == M - 1:
        mesta[row][num] = 0
        mesta[row][num - 1] = 0
    else:
        mesta[row][num] = 0
        mesta[row][num - 1] = 0
        mesta[row][num + 1] = 0
last = 0
for row in range(len(mesta)):
    if mx < sum(mesta[row]):
        last = row
        mx = sum(mesta[row])
    kol += sum(mesta[row])
print(kol, last + 1)
