with open('9/7350/7350.txt') as f:
    sp = [list(map(int, i.split())) for i in f.readlines()]


k = 0
for i in sp:
    povt = sum([x for x in i if i.count(x) > 1])
    if len(set(i)) < 6 and i.count(max(i)) == 1 and povt < sum(i) - povt:
        k += 1
print(k)
        