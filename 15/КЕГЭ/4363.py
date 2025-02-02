ans = []
A = range(30, 51)
P = range(10, 81)
for l in range(1, 100):
    for r in range(l + 1, 100):
        k = 0
        Q = list(range(l, r))
        for x in range(-150, 150):
            if (x in Q) <= ((x in A) and (not (x in P))):
                k += 1
        if k == 300:
            ans.append(len(Q))
print(min(ans))