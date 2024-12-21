from itertools import product
k = 0

for i in product('ABCDE', repeat=4):
    sogl = [j for j in i if j in 'BCD']
    glasn = [j for j in i if j in 'AE']
    sogl.sort()
    glasn.sort()
    ans = (glasn + sogl) == list(i)
    if ans:
        k += 1
print(k)