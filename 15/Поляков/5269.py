P = range(117, 159)
Q = range(129, 181)
# (x ∈ P) → ( ((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P)) )
a = []
for x in range(-1000, 1000):
    if ((x in P) <= ((((x in Q) and (not(x in a))) <= (not(x in P))))) == False:
        a.append(x)
print(a[-1] - a[0])