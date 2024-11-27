from fnmatch import fnmatch
def delitely(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(0, 10**9 + 1, 2801):
    if fnmatch(str(i), '9*31?5*7'):
        if delitely(sum([int(k) for k in str(i)])):
            print(i, i // 2801)