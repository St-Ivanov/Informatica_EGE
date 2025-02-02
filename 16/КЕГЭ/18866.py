a = [0] * 17000
for n in range(len(a)):
    if n < 100:
        a[n] = n ** 2
    elif n % 2 == 0:
        a[n] = 0.5 * a[n - 1]
    else:
        a[n] = 2 * a[n - 1]
print(1000 * a[16384] / a[7777])