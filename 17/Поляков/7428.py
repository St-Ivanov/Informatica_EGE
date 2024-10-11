with open('17/17-401.txt') as f:
    sp = [int(i) for i in f.readlines()]


mx = max([i for i in sp if abs(i) % 10 == 7])
ans = []
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if (((abs(x) % 2 == 1 )+ (abs(y) % 2 == 1) + (abs(z) % 2 == 1)) == 2 and ((x > mx) + (y > mx) + (z > mx)) == 1):
        ans.append(x)
        ans.append(y)
        ans.append(z)
print(len(ans) // 3, (str(sum(set(ans)) // len(set(ans))))[:3])