ans = []
for x in range(0, 25):
    for y in range(0, 25):
        for z in range(0, 25):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 15 and s.count('2') == 21:
                ans.append(x + y + z + 2)
print(max(ans))