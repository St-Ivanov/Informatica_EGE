a = [0] * 2000
for n in range(len(a)):
    if n < 4:
        a[n] = 1
    else:
        a[n] = a[n - 1] * (n - 3)
print(a[1401]/a[1397])