def f3(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
ans = []
for N in range(10, 10000):
    R = f3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += f3(sum(int(i) for i in R))
    R = int(R, 3)
    if R > 220:
        ans.append(R)
print(min(ans))