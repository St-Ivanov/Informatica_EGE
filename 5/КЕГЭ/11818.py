def f12(n):
    alf = '0123456789AB'
    s = ''
    while n != 0:
        s += alf[n % 12]
        n //= 12
    return s[::-1]
ans = []
for N in range(10, 10000):
    R = f12(N)
    if N % 4 == 0:
        R = '2' + R + '64'
    else:
        for letter in 'BA9876543210':
            if letter in R:
                R += letter
                break
    if int(R, 12) > 1799:
        ans.append(int(R, 12))
print(min(ans))