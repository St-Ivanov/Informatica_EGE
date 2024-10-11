ans = []

for N in range(1, 100):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += '01'
    else:
        R += '10'
    if int(R, 2) > 75:
        ans.append(int(R, 2))
print(min(ans))