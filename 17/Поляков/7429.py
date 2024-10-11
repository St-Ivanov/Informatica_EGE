with open('17/17-402.txt') as f:
    sp = [int(i) for i in f.readlines()]

ans = []

def sum_num(n):
    return sum([int(i) for i in str(n)])

mn = min([i for i in sp if len(str(i)) == 2 and i % sum_num(i) == 0])

for i in range(len(sp) - 1):
    if sp[i] % mn == 0 or sp[i + 1] % mn == 0:
        ans.append(sp[i] + sp[i + 1])

print(len(ans), max(ans))
