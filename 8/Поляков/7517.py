from itertools import product


num = 0
for i in product('КОСУФ', repeat=5):
    num += 1
    if i.count('Ф') == 0 and i.count('У') == 2:
        m = num
print(m)