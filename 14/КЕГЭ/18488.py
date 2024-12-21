def f(n):
    k = 0
    while n != 0:
        if n % 7 == 6:
            k += 1
        n //= 7
    return k
s = 7 ** 666 + 7 ** 333 - 343
for x in range(0, 1000):
    cop = s + 49 ** x
    if f(cop) == 49:
        print(x)
        break