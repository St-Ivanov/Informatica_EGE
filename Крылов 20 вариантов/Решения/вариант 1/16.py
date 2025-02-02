a = [0] * 2100
for n in range(1, len(a)):
    if n == 1:
        a[n] = 1
    else:
        a[n] = n * a[n - 1]
print(((a[2025] // 25) + a[2024]) // a[2023])