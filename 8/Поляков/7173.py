from itertools import permutations


k = 0
for i in permutations('ГЛУБИНА', r=7):
    if i.index('Г') - i.index('А') > 1:
        k += 1
print(k)