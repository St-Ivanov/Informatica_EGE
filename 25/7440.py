from itertools import product


for i in product('0123456789', repeat=3):
    num = int(f'12{i[0]}345{i[1]}67089{i[2]}')
    if num % 206 == 0:
        print(num, num // 206)