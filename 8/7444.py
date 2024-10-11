from itertools import product


k = 0
for i in product('01234567', repeat=6):
    s = ''.join(i)
    f = False
    t = True
    if i[0] != '0' and i.count('4') == 2 and '44' not in s and len(set(i)) == 5:
        for m in i:
            if f:
                if int(m) < 4:
                    t = False
                if int(m) == 4:
                    break
            if m == '4':
                f = True
        if t:
            k += 1
print(k)
                