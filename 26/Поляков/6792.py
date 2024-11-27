with open('26/Поляков/6792.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]

pos = [0] * 1440

for start, end in sp:
    for i in range(start, end + 1):
        pos[i] += 1
max_pos = max(pos)
k = 0
F = False
for i in pos:
    if F and i != max_pos:
        k += 1
        F = False
        continue
    else:
        if i == max_pos:
            F = True

print(k, max_pos)