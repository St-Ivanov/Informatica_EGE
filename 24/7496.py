with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\24-296.txt') as f:
    s = f.readline()
s = s.replace('AF','A F').split()
while '' in s:
    s.pop(s.index(''))
mn = 10 ** 10
for i in range(len(s) - 201):
    m = ''.join(s[i:i + 202])
    mn = min(mn, len(m))
print(mn)