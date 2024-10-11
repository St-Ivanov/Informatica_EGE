with open('17/17-375.txt') as f:
    sp = [int(i) for i in f.readlines()]


ans = []
mn = min([i for i in sp if len(str(i)) == 3 and len(set(list(str(i)))) == 3])
for i in range(len(sp) // 2):
    if (sp[i] * sp[-i - 1]) % mn == 0:
        ans.append(sp[i] + sp[-i - 1])
print(len(ans), min(ans))