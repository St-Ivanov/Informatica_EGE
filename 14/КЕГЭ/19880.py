def f(n):
    r = ''
    while n != 0:
        if n % 25 == 0:
            r += '0'
        else:
            r += '1'
        n //= 25
    return r[::-1]
print(str(int(f(15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005))).count('0'))