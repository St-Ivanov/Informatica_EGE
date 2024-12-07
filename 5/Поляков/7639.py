ans = []
for N in range(13):
    s = bin(N)[2:]
    if N % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    ans.append(int(s, 2))
print(max(ans))