from re import findall
mx = 0
for i in findall(r'(?:0|[1-4][0-4]*)(?:[-+](?:0|[1-4][0-4]*))*', open(r'Крылов 20 вариантов\Решения\вариант 1\24var01.txt').readline()):
    mx = max(mx, len(i))
print(mx)