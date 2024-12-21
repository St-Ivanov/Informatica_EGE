for n in range(100):
    s = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in s or '>2' in s or '>0' in s:
        s = s.replace('>3', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '3>', 1)
    ans = sum([int(i) for i in s[:-1]])
    if int(ans ** 0.5) == ans ** 0.5:
        print(n)
        break