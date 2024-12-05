with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-363.txt') as f:
    sp = [int(i) for i in f.readlines()]
def num(n, k):
    return min(list(str(n))) > max(list(str(k)))
def ch_nch(n):
    ch = [i for i in str(n) if int(i) % 2 == 0]
    nch = [i for i in str(n) if int(i) % 2 == 1]
    return len(ch) == len(nch)
mx = max([i for i in sp if ch_nch(i)])
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if num(x, y) and (x + y) <= mx:
        ans.append(x + y)
print(len(ans), max(ans))