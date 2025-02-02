mx = 0
for n in range(1, 10000):
    s = '1' + '9' * n
    while '19' in s or '49' in s or '999' in s:
        s = s.replace('19', '9', 1)
        s = s.replace('49', '91', 1)
        s = s.replace('999', '4', 1)
    sm = sum([int(i) for i in s])
    if sm > mx:
        print(sm)
        mx = sm
