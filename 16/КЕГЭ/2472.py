a = [0] * 10000
a[0] = 1
a[1] = 0
for n in range(2, len(a)):
    if n % 2 == 0:
        a[n] = a[n // 2] + 1
    else:
        a[n] = a[n // 2]
    if a[n] == 10:
        print(n)
        break