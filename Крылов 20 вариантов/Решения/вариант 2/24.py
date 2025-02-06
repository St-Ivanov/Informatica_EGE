from re import findall
mx = 0
for i in findall(r'(?:0|[5678][05678]*)(?:[-+](?:0|[5678][05678]*))*', open(r'Крылов 20 вариантов\Решения\вариант 2\24.txt').readline()):
    mx = max(mx, len(i))
print(mx)