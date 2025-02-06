def f(n):
    r = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            r.append(i)
            if n // i != i:
                r.append(n // i)
    r.sort()
    if r == []:
        return 0
    return r[0] + r[-1]
k = 0
for i in range(1000001, 10000000):
    M = f(i)
    if M % 10 == 6:
        print(i, M)
        k += 1
    if k == 5:
        break