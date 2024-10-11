def sc_12(n):
    s = '0123456789AB'
    ret = ''
    while n != 0:
        ret += s[n % 12]
        n //= 12
    return ret[::-1]


mx = 0
ans = []
for N in range(144, 1000):
    R = sc_12(N)
    if N % 12 == 0:
        R += R[-3:]
    else:
        R = sc_12(N % 12 * 3) + R
    if int(R, 12) < 58000 and mx < int(R, 12):
        mx = int(R, 12)
        ans.append(N)
print(max(ans))
