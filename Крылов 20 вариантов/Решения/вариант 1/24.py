with open(r'C:\Users\si655\OneDrive\Документы\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\24var01.txt') as f:
    s = f.readline()
last = ''
lens = 0
mx = 0
for el in s:
    if (last == '-') or (last == '+' and el == '+') or (last == '+' and el == '0'):
        last = el
        lens = 1
    else:
        lens += 1
        mx = max(mx, lens)
        last = el
print(mx)