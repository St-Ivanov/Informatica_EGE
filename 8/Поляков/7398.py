from itertools import permutations

k = 0
s = set()
for i in permutations('АААВВРР', r=7):
    i = ''.join(i)
    if i not in s:
        k += 1
        s.add(i)
        if i.count('ААА') == 1 and i.count('РР') == 0 and i[0] == 'В' and k % 2 == 0:
            print(i, k)