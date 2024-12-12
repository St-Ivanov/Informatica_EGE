def f(a):
    a = a[::-1]
    return sum([a[i] * 19 ** i for i in range(len(a))])


for x in range(19):
    num1 = [9, 8, 8, 9, 7, x, 2, 1]
    num2 = [2, x, 9, 2, 3]
    if (f(num1) + f(num2)) % 18 == 0:
        print((f(num1) + f(num2)) // 18)
