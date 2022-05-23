import random

Pole = []
for i in range(8):
    Pole.append(random.randint(0,9))
Pole.sort()
print(Pole)

maxnum = ""
minnum = ""
for n in Pole:
    minnum += str(n)
    maxnum = str(n) + maxnum

print(int(maxnum) - int(minnum))