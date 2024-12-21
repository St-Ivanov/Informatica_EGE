with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\9756\9756.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
t = max([i[1] for i in sp])
time = [True] * (t + 1)
for i in range(len(sp)):
    sp[i].append(sp[i][1] - sp[i][0])
sp.sort(key=lambda x: x[2])
count = 0
mx = 0
st = 0
for start, end, _ in sp:
    if all(time[start:end]):
        for i in range(start, end):
            time[i] = False
        count += 1
        if mx < end:
            mx = end
            pr_st = st
            st = start
last_conf = [i for i in sp if i[0] >= pr_st]
ans = max([i[1] for i in last_conf])
print(count, ans)