with open("Day1\Day1.txt","r") as f:
    Depths = []
    for line in f:
        Depths.append(int(line))


Counter = 0
for i in range(1,len(Depths),1):
    if Depths[i] > Depths[i-1]:
            Counter += 1

print(Counter)

Counter = 0
for i in range(3,len(Depths),1):
    if Depths[i] + Depths[i-1] + Depths[i-2] > Depths[i-1] + Depths[i-2] + Depths[i-3]:
            Counter += 1

print(Counter)