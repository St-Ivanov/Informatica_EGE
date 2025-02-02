def f(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return sum(ret)

for i in range(1000, 10000):
    s = f(i)
    if s % 100 == 23:
        print(i, s)