ArrayOfNumbers = []
from random import randint
for i in range(10):
    ArrayOfNumbers.append(randint(0,1000))
print(ArrayOfNumbers)


ArrayOfNumbers.sort()
SearchNum = 500
while len(ArrayOfNumbers) >0:
    if SearchNum == ArrayOfNumbers[len(ArrayOfNumbers)//2]:
        print("It's there")
        break
    elif SearchNum > ArrayOfNumbers[len(ArrayOfNumbers)//2]:
        ArrayOfNumbers = ArrayOfNumbers[len(ArrayOfNumbers)//2 + 1:]
    else:
        ArrayOfNumbers = ArrayOfNumbers[0:len(ArrayOfNumbers)//2]
print(ArrayOfNumbers)
if len(ArrayOfNumbers) == 0:
    print("It's not there")