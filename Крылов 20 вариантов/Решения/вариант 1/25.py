def f(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    ret.sort()
    for i in ret:
        if i != 7 and i != n and i % 10 == 7:
            return True, i
    return False, 0
k = 0
for i in range(700000, 1000000):
    s = f(i)
    if s[0]:
        print(i, s[1])
        k += 1
    if k == 5:
        break