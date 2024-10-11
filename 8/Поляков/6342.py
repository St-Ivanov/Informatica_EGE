from itertools import permutations


ans = []
for i in permutations('ДОБРЫНЯ', r=6):
    s = ''.join(i)
    if sum([i.count('О'), i.count('Ы'), i.count('Я')]) < 3 and not('ОА' in s or 'ОЯ' in s or 'ЫО' in s or 'ЫЯ' in s or 'ЯО' in s or 'ЯЫ' in s):
        ans.append(s)
print(len(ans))