with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\КЕГЭ\13085\1.txt') as f:
    s = f.readline()
s = s.replace('X', 'X ')
s = s.replace('Y', 'Y ')
s = s.split()
mx = 0
for i in range(len(s)-2):
    prom = s[i] + s[i + 1] + s[i + 2]
    prom = prom[:-1]
    if prom.count('Y') == 1 and prom.count('X') == 1:
        mx = max(mx, len(prom))
print(mx)