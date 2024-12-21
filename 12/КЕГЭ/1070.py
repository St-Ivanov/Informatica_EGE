# еденица даёт 2 двойки и еденицу, двойка даёт одну еденичку
s = '0' + '1' * 32 + '2' * 8
cop = s
while '01' in s or '02' in s:
    s = s.replace('01', '2202', 1)
    s = s.replace('02', '10', 1)
print(s.count('1'), s.count('2'))
print(cop.count('2'))