with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-378.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = abs(max([i for i in sp if abs(i) % 1001 == 0], key=abs))
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if len(str(abs(x))) == 3 or len(str(abs(y))) == 3:
        if x + y > mx:
            ans.append(x + y)
print(len(ans), min(ans))