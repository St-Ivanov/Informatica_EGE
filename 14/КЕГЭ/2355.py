n = 3 * 64 ** 1073 - 2 * 16 ** 1131 + 4 ** 1173 - 484
s = ''
while n != 0:
    s += str(n % 4)
    n //= 4
s = list(s)
mx = max(s, key=lambda x: s.count(x))
mn = min(s, key=lambda x: s.count(x))
print(s.count(mx) - s.count(mn))