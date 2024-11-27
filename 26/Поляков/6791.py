with open('26/Поляков/6791.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]

lst = []
for i in range(N):
    lst.append([sp[i][0], i + 1, 0])
    lst.append([sp[i][1], i + 1, 1])

ans = []
index = 0
l = []
r = []
lst.sort(key=lambda x: x[0])
while lst != []:
    start, id, typ = lst.pop(0)
    index = id
    for i in range(len(lst)):
        if lst[i][1] == id:
            lst.pop(i)
            break
    if typ == 1:
        l.append(id)
    else:
        r = [id] + r
ans = l + r
print(index, len(r) - r.index(index) - 1)