min__ = 10**10
with open('27/demo_2025_27_А.txt') as f:
    f.readline()
    sp = [list(map(float, i.replace(',', '.').split())) for i in f.readlines()]

for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp) - 1):
        center1 = sp[i]
        center2 = sp[j]
        summ = 0
        for point in sp:
            d1 = ((point[0] - center1[0]) ** 2 + (point[1] - center1[1]) ** 2) ** 0.5
            d2 = ((point[0] - center2[0]) ** 2 + (point[1] - center2[1]) ** 2) ** 0.5
            summ += min(d1, d2)
        if summ < min__:
            ans = [center1, center2]
            min__ = summ
print((ans[0][0] + ans[1][0]) / 2 * 10000, (ans[0][1] + ans[1][1]) / 2 * 10000)
 