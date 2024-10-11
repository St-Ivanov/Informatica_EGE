with open('9/7547/7547.txt') as f:
    sp = [list(map(int, i.split())) for i in f.readlines()]\


k = 0
for i in sp:
    if max(i) + min(i) <= sum(i) - max(i) - min(i):
        k += 1
print(k)