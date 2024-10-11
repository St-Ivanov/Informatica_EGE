def f(n):
    return sum([int(i) for i in n])


for n in range(2, 1000, 2):
    s = '>2' + '12' * n + '<'
    while not ('>2<' in s):
        s = s.replace('>1', '>2', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('1<', '<2', 1)
    s = s.replace('>', '')
    s = s.replace('<', '')
    if f(s[1:-1]) > 103:
        print(n)
        break