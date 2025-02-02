lens = 0
mx = 0
for n in range(51, 100):
    s = '5' * n
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    if mx < s.count('5'):
        mx = s.count('5')
        lens = n
print(lens)