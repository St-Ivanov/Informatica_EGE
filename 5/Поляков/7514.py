ans = []

for N in range(1, 12):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '10'
    else:
        R = '1' + R + '01'
    ans.append(int(R, 2))
print(max(ans))
