def sc_45(n):
    ret = []
    while n != 0:
        ret.append(n % 45)
        n //= 45
    return ret[::-1]


def new_int(a, k):
    a = a[::-1]
    summ = 0
    for i in range(len(a)):
        summ += a[i] * k ** i
    return summ


ans = []
for N in range(1001, 2000):
    R = sc_45(N)
    ch, nch = [], []
    for i in range(0, len(R), 2):
        ch.append(R[i])
    for i in range(1, len(R), 2):
        nch.append(R[i])
    if new_int(ch, 45) > new_int(nch, 45):
        R = nch + R + ch
    else:
        R = ch + R + nch
    ans.append(new_int(R, 45))
print(min(ans))
