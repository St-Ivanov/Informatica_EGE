with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\24-228.txt') as f:
    s = f.readline()
mx = ''
last = -1
for i in range(len(s) - 1):
    if s[i] == 'S' and s[i + 1] == 'S':
        if last != - 1:
            s1 = s[last + 2:i]
            if len(s1) == 11 and s1.isdigit():
                if s1[:2] == '12' and s1[6:8] == '77' and s1[10] == '9':
                    mx = max(mx, s1)
        last = i
m = 1
sm = 0
for c in mx:
    if int(c) % 2 == 1:
        sm += int(c)
    else:
        m *= int(c)
print(sm + m)