from itertools import permutations

num = 0
k = 0
a = []
for i in permutations('АААВВРР', r=7):
    num += 1
    s = ''.join(i)
    a.append(s)
a = list(set(a))
a.sort()
num = 0
for i in a:
    num += 1
    if (num % 2 == 0) and (i[0] == 'В') and ('ААА' in i) and ('РР' not in i):
        k = num
print(k)
