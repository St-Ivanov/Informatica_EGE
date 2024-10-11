from itertools import product


k = 0
ans = 0
for i in product('АБОРСУЭ', repeat=5):
    k += 1
    s = ''.join(i)
    if k % 2 == 0 and i.count('У') == 0 and i.count('Р') >= 2 and \
        ('РАР' in s or 'РБР' in s or 'РОР' in s or 'РСР' in s or 'РЭР' in s):
        ans += 1
print(ans)