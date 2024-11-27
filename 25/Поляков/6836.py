for i in range(10**10 + 10 ** 9, 10**11):
    if i % 2023 == 0:
        start = i
        break

from fnmatch import fnmatch

ans = []
for i in range(start, 10**11, 2023):
    if fnmatch(str(i), '1*1'):
        ans.append(i)
mx = max(ans, key=lambda x: sum([int(k) for k in str(x)]))
fil = list(filter(lambda x: sum([int(k) for k in str(x)]) == mx, ans))
print(fil)