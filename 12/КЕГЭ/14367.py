for n in range(4, 10000):
    s = '5' + '4' * n
    while '54' in s or '4444' in s or '7744' in s:
        s = s.replace('54', '77', 1)
        s = s.replace('4444', '5', 1)
        s = s.replace('7744', '45', 1)
    ans = sum([int(i) for i in s])
    if int(ans ** 0.5) == ans ** 0.5:
        print(n)
        break