a = [0] * 2300
for n in range(len(a)):
    if n < 3:
        a[n] = 2
    else:
        a[n] = 2 * a[n - 2]
print(a[2222] / a[2182])