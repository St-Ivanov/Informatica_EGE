with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\24-296.txt') as f:
    s = f.readline()
s = s.replace('CD', '*')
s = s.split('*')
mx = 0
for i in range(len(s) - 160):
    l = ''.join(s[i:i+161]).replace('*', '') + 'CD' * 160 + 'CD'
    mx = max(mx, len(l))
print(mx)