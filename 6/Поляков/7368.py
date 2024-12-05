pole = [0] * 1000

x = 100
for i in range(11):
    x += 2
    pole[x] = 1
    x -= 4
    pole[x] = 1
    x += 2
    x += 2
print(sum(pole))