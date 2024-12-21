def f(n):
    k = 0
    while n != 0:
        if n % 5 == 4:
            k += 1
        n //= 5
    return k
s = 125 ** 200 + 74
for x in range(1, 1000):
    if f(s - 5 ** x) == 100:
        print(x)
        break