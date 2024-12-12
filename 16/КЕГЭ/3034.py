def f(x, y):
    if len(x) == y:
        return x.count('0') == 3 and int(x, 2) <= 10 ** 9
    count = 0
    if x.count('0') < 3:
        count += f(x + '1', y) + f(x + '0', y)
    if x.count('0') == 3:
        count += (int(x + '1' * (y - len(x)), 2) <= 10 ** 9)
    return count

ans = 0
for i in range(4, 31):
    ans += f('1', i)
print(ans)