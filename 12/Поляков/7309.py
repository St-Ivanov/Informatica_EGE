ans = []
for x in range(20):
    for y in range(20):
        for z in range(20):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            cop = s
            while '00' not in s:
                s = s.replace('01', '130', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '210', 1)
            if s.count('1') == 28 and s.count('2') == 18:
                ans.append(cop)
print(len(min(ans, key=len)))