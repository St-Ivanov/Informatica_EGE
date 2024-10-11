with open('9/7518/7518.txt') as f:
    sp = [list(map(int, i.split())) for i in f.readlines()]


k = 0
for i in sp:
    if len(set(i)) == 4:
        mx = 0
        for m in set(i):
            if i.count(m) == 3:
                mx = m
                break
        if (mx * 3) ** 2 > ((sum(i) - m * 3) ** 2):
            k += 1
print(k)