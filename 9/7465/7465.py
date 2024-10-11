with open('9/7465/7465.txt') as f:
    sp = [list(map(int, i.split())) for i in f.readlines()]


k = 0
for i in sp:
    if len(set(i)) == 3 and max(i) < sum(i) - max(i):
        k += 1
print(k)
