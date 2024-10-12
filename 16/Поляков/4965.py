kol = 0
for i in range(30):
    for j in range(i + 1, 30):
        for k in range(j + 1, 30):
            s = 2 ** i + 2 ** j + 2 ** k
            if 1 <= s <= 500_000_000:
                kol += 1
print(kol)
# или
from math import factorial
print((factorial(29))/(factorial(3)*(factorial(29 - 3)))) # C из n по k