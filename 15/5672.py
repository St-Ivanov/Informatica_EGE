B = range(10, 41)
a = []
for x in range(1, 301):
    if (x in a) or ((x in B) <= (not (x % 6 == 0))) == False:
        a.append(x)
print(a[-1]-a[0])