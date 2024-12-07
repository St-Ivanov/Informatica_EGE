def f(n):
    s = ''
    while n != 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]


for N in range(10, 10000):
    s = f(N)
    if N % 4 == 0:
        s += s[-2:]
    else:
        s += f(N % 4 * 5)
    if int(s, 4) < 555:
        print(N)
