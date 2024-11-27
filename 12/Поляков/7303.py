def sum_s(n):
    return sum([int(i) for i in n])


ans = []
for x in range(0, 100):
    for y in range(0, 100):
        s = '0' + '1' * x + '2' * y
        cop = s
        if len(s) >= 95:
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1)
                s = s.replace('01', '2210', 1)
            m = sum_s(s)
            if str(m) == str(m)[::-1]:
                ans.append(sum_s(cop))
print(min(ans))
