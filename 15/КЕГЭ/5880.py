def f(x, y, z):
    a = [x, y, z]
    a.sort()
    if a[0] + a[1] > a[2]:
        return True
    return False
for A in range(1000, 1, -1):
    k = 0
    for x in range(1, 1000):
        if (f(A, 5, x)) <= ((max(x, 11) <= 19) == (not (f(23, 13, x)))):
            k += 1
    if k == 999:
        print(A)
        break