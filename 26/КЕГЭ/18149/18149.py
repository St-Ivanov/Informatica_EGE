with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\18149\18149.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
for i in range(len(sp)):
    sp[i].append(sum(sp[i][1:]))
sp.sort(key=lambda x: (x[5], x[1], x[2] + x[4]), reverse=True)
ans = max([i[0] for i in sp if sp.index(i) > 299 and i[1] == sp[299][1]])
print(sp[299][0], ans)
