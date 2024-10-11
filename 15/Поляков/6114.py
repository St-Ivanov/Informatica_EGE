B = list(range(23, 38))
C = list(range(41, 74))
a = []
for x in range(-1000, 1000):
    if not(((not(x in B)) <= (x in C)) <= (x in a)) == True:
        a.append(x)
print(a[-1] - a[0]) 