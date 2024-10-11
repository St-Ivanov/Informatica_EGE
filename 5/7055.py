def sc_3(n):
    ret = ''
    while n != 0:
        ret += str(n % 3)
        n //= 3
    return ret[::-1]


for N in range(1, 1000):
    R = sc_3(N)
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R += str(sc_3(sum(list(map(int, R)))))
    if int(R, 3) > 168:
        print(N)
        break
