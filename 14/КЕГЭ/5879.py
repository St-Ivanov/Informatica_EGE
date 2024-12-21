def f(a, k):
    a = a[::-1]
    return sum([a[i] * k ** i for i in range(len(a))])
def f3(n):
    alf = '0123456789ABC'
    s = ''
    while n != 0:
        s += alf[n % 13]
        n //= 13
    return s[::-1]

for x in range(4, 10):
    num1 = f([3, x, 1, 5, x], 15)
    num2 = f([1, 2, 3], int(f'3{x}51'))
    num3 = f([1, x, 3], int(f'1{x}3'))
    num4 = f([1, x, 2], x + 1)
    sm = num1 + num2 + num3 + num4 + x ** x
    if sm % 13 == 0:
        print(f3(sm))