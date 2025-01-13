with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\КЕГЭ\10105\1.txt') as f:
    s = f.readline()
a = []
for i in range(len(s)):
    if s[i] == 'T':
        a.append(i)
mx = 0
for i in range(len(a) - 99):
    mx = max(mx, a[i + 99] - a[i] + 1)
print(mx)