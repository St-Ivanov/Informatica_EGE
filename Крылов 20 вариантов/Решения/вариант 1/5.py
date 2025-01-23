for N in range(100):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R.replace('1', '11')
    else:
        R = R.replace('0', '00')
    if int(R, 2) > 70:
        print(N)
        break