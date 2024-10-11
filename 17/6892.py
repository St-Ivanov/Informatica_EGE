def summ_num(n):
    return sum([int(i) for i in str(n)])


with open('17/17-385.txt') as f:
    sp = [int(i) for i in f.readlines()]

mn = 5425225
mx = 0
mx = (min(sp, key=lambda x: summ_num(x)))
ans = []
for i in range(len(sp) - 1):
    if sp[i] > mx and sp[i + 1] > mx:
        ans.append(summ_num(sp[i]) + summ_num(sp[i + 1]))
print(len(ans), max(ans))
