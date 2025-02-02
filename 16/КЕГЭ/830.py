a = [0] * 10000
count = 0
for n in range(1, 10000, 2):
    if n < 3:
        a[n] = n + 1
    elif n % 2 == 0:
        a[n] = n + 2 * a[n + 2]
    else:
        a[n] = a[n - 2] + n - 2
    if len(str(a[n])) == 3:
        count += 1
print(count)