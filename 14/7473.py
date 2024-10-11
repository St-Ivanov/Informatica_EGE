def ch_31(n):
    ret = []
    while n != 0:
        ret.append(n % 31)
        n //= 31
    return ret


s = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
print(sum(filter(lambda x: x <= 17, ch_31(s))))