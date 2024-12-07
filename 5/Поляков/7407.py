def f(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


ans = []
for N in range(1, 1000):
    s = f(N)
    if N % 2 == 0:
        s = '2' + s + f(int(s[-1]) * 2)
    else:
        s = f(int(s[0]) * 2) + s + '2'
    R = int(s, 3)
    if R > 100:
        ans.append(R)
print(min(ans))
