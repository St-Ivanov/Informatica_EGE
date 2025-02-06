a = [0] * 3100
for n in range(len(a)):
    if n == 1:
        a[n] = 1
    else:
        a[n] = n * a[n - 1]
print(((a[3000] // 150) + a[2999]) / a[2998])