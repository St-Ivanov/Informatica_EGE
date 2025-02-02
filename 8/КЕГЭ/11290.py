from itertools import product
delt = [i + j for i in '02468ACE' for j in '02468ACE'] + [i + j for i in '13579BDF' for j in '13579BDF']
count = 0
for i in product('0123456789ABCDEF', repeat=4):
    if i[0] != '0':
        if i.count('9') == 1:
            f = True
            for k in delt:
                if k in ''.join(i):
                    f = False
                    break
            if f:
                count += 1
print(count)