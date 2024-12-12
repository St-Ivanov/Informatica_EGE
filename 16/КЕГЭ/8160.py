a = [0] * 3100
for n in range(len(a) - 1, 0, -1):
    if n > 3000:
        a[n] = n
    elif n % 2 == 0:
        a[n] = n + a[n + 1] + 1
    else:
        a[n] = a[n + 2] + 2
print(a[40] - a[43])