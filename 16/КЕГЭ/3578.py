a = [0] * 40
for n in range(len(a)):
    if n < 3:
        a[n] = 1
    elif n % 2 == 0:
        a[n] = a[n - 1] + n - 1
    else:
        a[n] = a[n - 2] + 2 * n - 2
print(a[31])