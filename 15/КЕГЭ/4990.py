B = range(10, 41)
ans = []
for l in range(0, 50):
    for r in range(l + 1, 50):
        A = range(l, r)
        k = 0
        for x in range(1, 301):
            if (x in A) or ((x in B) <= (not(x % 6 == 0))):
                k += 1
        if k == 300:
            ans.append(len(A))
print(min(ans) - 1)