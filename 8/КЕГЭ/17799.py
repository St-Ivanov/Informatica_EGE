from itertools import product
num = 0
alf = ''.join(sorted(list('АРГУМЕНТ')))
for i in product(alf, repeat=4):
    num += 1
    if len(set(i)) == 4:
        if sorted(list(i)) == list(i):
            last = num
print(last)