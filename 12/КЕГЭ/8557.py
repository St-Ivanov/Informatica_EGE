lens = 0
mx = 0
for n in range(1, 100):
    s = '13' * n
    while '13' in s or '31' in s or '11' in s:
        s = s.replace('13', '4', 1)
        s = s.replace('31', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('44', '1', 1)
    sm = sum([int(i) for i in s])
    if len(str(sm)) == 2 and mx < sm:
        mx = sm
        lens = n
print(lens)