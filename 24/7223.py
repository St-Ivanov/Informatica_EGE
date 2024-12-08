with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\24-280.txt') as f:
    s = f.readline()
dop = ''
ans = []
for i in range(len(s)):
    if s[i] in dop:
        id = dop.index(s[i])
        ans.append(dop)
        dop = dop[id + 1:]
    dop += s[i]
print(len(max(ans, key=len)))
