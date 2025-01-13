with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\КЕГЭ\17750\17750.txt') as f:
    sp = [int(i) for i in f.readlines()]
ans = []
mn = min(sp)
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if (x % 77 + y % 77) == mn:
        ans.append(x + y)
print(len(ans), max(ans))