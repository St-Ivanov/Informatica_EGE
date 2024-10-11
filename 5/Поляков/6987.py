ans = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '00'
    else:
        R += '11'
    if int(R, 2) > 204:
        ans.append(int(R,2))
print(min(ans))
