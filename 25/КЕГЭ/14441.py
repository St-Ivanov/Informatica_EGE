from fnmatch import fnmatch
def f(n):
    r = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            r.append(i)
            if n // i != i:
                r.append(n // i)
    return sum(r)
for i in range(0, 10 ** 9, 2068):
    s = f(i)
    if fnmatch(str(i), '193*7?') and s % 7 == 0:
        print(i, s)