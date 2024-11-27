def subfactorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (subfactorial(n - 1) + subfactorial(n - 2))


print(subfactorial(12))