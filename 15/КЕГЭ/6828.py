P = range(257, 357)
Q = range(5, 601)
R = range(59, 229)
ans = []
for l in range(600):
    for r in range(l + 1, 600):
        A = range(l, r)
        k = 0
        for x in range(600):
            if((x in R) <= (x in A)) or (((x % 3 == 0) <= (x in P)) <= ((x in Q) <= (x in A))):
                k += 1
        if k == 600:
            ans.append(len(A))
            break
print(min(ans) - 1)