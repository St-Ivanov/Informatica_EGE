def f(n):
    k = 0
    while n != 0:
        if n % 6 == 0:
            k += 1
        n //= 6
    return k
s = 6 ** 260 + 6 ** 160 + 6 ** 60
for x in range(2031):
    cop = s - x
    if f(cop) == 202:
        print(x)
        break