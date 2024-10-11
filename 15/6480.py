ans = []
P = range(10, 22)
Q = range(13, 39)
R = range(18, 26)
for left in range(0, 100):
    for right in range(left + 1, 100):
        A = list(range(left, right))
        k = 0
        for x in range(1000):
            if (not((x in Q) <= ((x in P) or (x in R)))) <= ((not(x in A)) <= (not(x in Q))):
                k += 1
        if k == 1000:
            ans.append(len(A))
print(min(ans))