ans = []
for N in range(0, 256):
    R = ('0' * 8 + bin(N)[2:])[-8:]
    R = R.replace('0', '*')
    R = R.replace('1', '0')
    R = R.replace('*', '1')
    if int(R, 2) % 5 == 0:
        R = '100' + R[3:]
    else:
        R = '101' + R[3:]
    if int(R, 2) == 180:
        ans.append(N)
print(len(ans))
