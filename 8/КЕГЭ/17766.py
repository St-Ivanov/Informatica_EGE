from itertools import product
num = 0
for i in product('БЕНРСТЬЯ', repeat=5):
    num += 1
    if num % 2 == 0 and i[0] == 'Р' and i.count('Ь') == 0:
        last = num
print(last)