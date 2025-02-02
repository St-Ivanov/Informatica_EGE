def f(n):
    k = 0
    while n != 0:
        if n % 9 == 5:
            k += 1
        n //= 9
    return k
print(f(361 * 2349 ** 84 - 89 ** 192 + 1953 ** 481 * 4843 ** 151))