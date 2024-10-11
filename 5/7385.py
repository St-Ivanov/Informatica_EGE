def sc_4(n):
    ret = ''
    while n != 0:
        ret += str(n % 4)
        n //= 4
    return ret[::-1]


ans = []
mx = 0
for N in range(1, 1000):
    R = sc_4(N)
    if N % 4 == 0:
        R += R[-2:]
    else:
        R += sc_4(N % 4 * 5)
    if int(R, 4) < 555 and mx <= int(R, 4):
        mx = int(R, 4)
        ans.append(N)
print(max(ans))
