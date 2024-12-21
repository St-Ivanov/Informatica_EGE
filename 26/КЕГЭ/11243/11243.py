with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\11243\11243.txt') as f:
    K, N = [int(i) for i in f.readline().split()]
    sp = [[int(j) for j in i.split()] for i in f.readlines()]
couriers = [0] * K
sp.sort(key=lambda x: x[0])
count = 0
for start, end in sp:
    couriers.sort()
    if start >= couriers[0]:
        couriers[0] = start + 2 + end * 2
        last = start + 2 + end
    else:
        if couriers[0] + end <= 1440:
            count += 1
        couriers[0] += 2 + end * 2
print(count, last)