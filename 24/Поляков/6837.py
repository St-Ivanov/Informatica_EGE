with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\24-275.txt') as f:
    s = f.readline()
s = s.replace('XYZ', ' ')
s = s.split()
ans = []
for m in s:
    while m[0] in 'XYZ' or m[-1] in 'XYZ':
        if m[0] in 'XYZ':
            m = m[1:]
        if m[-1] in 'XYZ':
            m = m[:-1]
    ans.append(m)
print(len(max(ans, key=len)))