from itertools import product
k = 0
for i in product('АВИКПРЧЫ', repeat=5):
    s = ''.join(i)
    k += 1
    if 'А' not in s and 'И' not in s and 'Ы' not in s and k % 5 != 0:
        if len(set(s)) == 5:
            print(k - k // 5)
            break
