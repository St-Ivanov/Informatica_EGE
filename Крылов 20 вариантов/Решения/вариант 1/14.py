def f(n):
    count = 0
    while n != 0:
        count += n % 9 == 0
        n //= 9
    return count == 1026

s = 9 ** 2025 + 9 ** 1000
for x in range(5769, 0, -1):
    l = s - x
    if f(l):
        print(x)
        break