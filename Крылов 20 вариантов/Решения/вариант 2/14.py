def f(n):
    k = 0
    while n != 0:
        if n % 5 == 0:
            k += 1
        n //= 5
    return k == 527
s = 5 ** 2025 + 5 ** 1500
for x in range(2735, 0, -1):
    l = s - x
    if f(l):
        print(x)
        break