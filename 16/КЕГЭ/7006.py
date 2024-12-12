a = [0] * 10000
for n in range(len(a)):
    if n == 1:
        a[n] = 3
    elif n % 2 == 0:
        a[n] = a[n - 1] + 5 * (n - 1)
    else:
        a[n] = a[n - 1] + 7
print(a[8765])