s = list('0123456789qwertyuiopasdfghjklzxcvbnm')
s.sort()
for x in s:
    s1 = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
    if s1 % 21 == 0:
        print(s1 // 21)
        break