ans = []
for A in range(-100, 100):
    k = 0
    for x in range(-150, 150):
        for y in range(-150, 150):
            if ((A < x) or ((x ** 2 - 7 * x + 10) > 0)) and ((A >= y) or ((y ** 2 + 7 * y + 12) > 0)):
                k += 1
    if k == 90000:
        ans.append(A)
print(len(ans))