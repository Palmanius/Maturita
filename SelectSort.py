import random
SetOfNum = []
for i in range(500):
    SetOfNum.append(random.randint(0,500))
print(SetOfNum)

sortedNums = []

while len(SetOfNum) > 0:
    lowest = 999999999
    for i in SetOfNum:
        if i < lowest:
            lowest = i
    sortedNums.append(lowest)
    SetOfNum.remove(lowest)

print(sortedNums)