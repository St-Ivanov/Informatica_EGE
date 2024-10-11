def suml(n):
    return sum([int(i) for i in n])

for n in range(1, 100):
    s = '>' + '0' * 12 + '1' * n + '2' * 8
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>')
        s = s.replace('>2', '2>')
        s = s.replace('>0', '1>')
    if suml(s[:-1]) == 68:
        print(n)
