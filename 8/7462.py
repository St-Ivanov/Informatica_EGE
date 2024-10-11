from itertools import product


zap = ['01', '03', '05', '07', '10', '30', '50', '70']
kol = 0
for i in product('012345678', repeat=5):
    if i[0] != '0' and i.count('0') == 1:
        m = ''.join(i)
        flag = True
        for x in zap:
            if x in m:
                flag = False
        if flag:
            kol += 1
print(kol)
