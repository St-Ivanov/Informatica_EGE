def sc_5(n):
    ret = ''
    while n != 0:
        ret += str(n % 5)
        n //= 5
    return ret[::-1]


ans = []
for N in range(1, 1000):
    R = sc_5(N)
    if N % 5 == 0:
        R += R[-2:]
    else:
        R += sc_5(N % 5 * 7)
    if int(R, 5) > 200:
        ans.append(int(R, 5))
print(min(ans))
