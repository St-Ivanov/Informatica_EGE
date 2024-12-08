def f(n):
    k = 0
    while n != 0:
        if n % 7 == 0:
            k += 1
        n //= 7
    return k
s = 7 ** 170 + 7 ** 100
for x in range(2030, 0, -1):
    m = s - x
    if f(m) == 71:
        print(x)
        break