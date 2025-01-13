for N in range(0, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R += '100'
    else:
        R += '011'
    if int(R, 2) > 300:
        print(N)
        break