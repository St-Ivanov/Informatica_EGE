from itertools import permutations
count = 0
for lens in [3, 5]:
    for i in permutations('0123456789ABCDEF', r=lens):
        if i[0] != '0':
            i = list(i)
            if sorted(i, reverse=True) == i:
                count += 1
print(count)