from itertools import product
k = 0
for i in product('АЙЛМ', repeat=5):
    k += 1
    s = ''.join(i)
    if 'ЙЙ' not in s and s.count('М') == 0 and s.count('Л') == 0:
        print(k)