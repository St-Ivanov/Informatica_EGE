from itertools import product


kol = 0
for i in product('012345678', repeat=6):
    if i[0] not in '01357' and i[-1] not in '23' and i.count('1') >= 2:
        kol += 1
print(kol)
