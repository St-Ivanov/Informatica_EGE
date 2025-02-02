from fnmatch import fnmatch
def f(n):
    r = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            r.append(i)
            if n // i != i:
                r.append(n // i)
    return sorted(r)
for x in range(int((10 ** 9) ** 0.5)):
    if fnmatch(str(x ** 2), '15*3*09') and len(f(x ** 2)) == 9:
        print(x ** 2, f(x ** 2)[-2])