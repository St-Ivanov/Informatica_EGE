from itertools import product

k = 0
for i in product('КОСУФ', repeat=5):
    k += 1
    if i.count('Ф') == 0 and i.count('У') == 2:
        print(k)