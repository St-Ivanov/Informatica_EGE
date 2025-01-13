def f6(n):
    s = ''
    while n != 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
ans = []
for N in range(10, 10000):
    R = f6(N)
    if N % 3 == 0:
        R += R[:2]
    else:
        R += f6((N % 3) * 10)
    if int(R, 6) > 680:
        ans.append(int(R, 6))
print(min(ans))
