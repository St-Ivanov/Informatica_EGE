ans = set()
for i in range(4, 1000):
    s = '7' + '6' * i
    while '766' in s or '667' in s:
        s = s.replace('766', '67', 1)
        s = s.replace('667', '7', 1)
    ans.add(s)
print(len(ans))