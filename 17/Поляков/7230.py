with open('17/17-390.txt') as f:
    sp = [int(i) for i in f.readlines()]


ans = []
sr_sp = [i for i in sp if abs(i) % 100 == 28]
sr = sum(sr_sp) / len(sr_sp)
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if ((len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) + (len(str(abs(z))) == 4)) > 0 and \
       ((abs(x) % 100 == 11) + (abs(y) % 100 == 11) + (abs(z) % 100 == 11)) == 2 and \
       x > sr and y > sr and z > sr:
        ans.append(x + y + z)
print(len(ans), min(ans))