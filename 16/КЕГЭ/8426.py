g = [0] * 100000
f = [0] * 2000001

for n in range(2000000, 0, -1):
    if n > 1000000:
        f[n] = n
    else:
        f[n] = n + f[2 * n]
for n in range(1, len(g)):
    g[n] = f[n] / n
k = 0
s = g[2000]
for n in range(1, 20000):
    if g[n] == s:
        k += 1
print(k)