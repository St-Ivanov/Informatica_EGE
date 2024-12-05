with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\Авторские\13\1.txt') as f:
    K, N = [int(j) for j in f.readline().split()]
    spisok = [[int(j) for j in i.split()] for i in f.readlines()]

rooms = [0] * K

spisok.sort()
last = 0
prostoi = []
for start, end in spisok:
    r = 0
    for i in range(K):
        if rooms[i] <= rooms[r]:
            r = i
    if end > rooms[r] and start <= 10080 and rooms[r] <= 10080:
        last = r + 1
        prostoi.append(rooms[r] - start + 1)
        rooms[r] = end + 30
print(max(prostoi), last)