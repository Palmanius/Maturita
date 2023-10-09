ArrayOfNumbers = []
from random import randint
for i in range(10):
    ArrayOfNumbers.append(randint(0,1000))
print(ArrayOfNumbers)
done = False
sorted = 0

for i in range(len(ArrayOfNumbers)):
    done = True

    for index,num in enumerate(ArrayOfNumbers[0:len(ArrayOfNumbers)-sorted]):
        if index>0:
            if num < ArrayOfNumbers[index-1]:
                done = False
                ArrayOfNumbers[index] = ArrayOfNumbers[index-1]
                ArrayOfNumbers[index-1] = num
    sorted +=1
    if done: break
    print(ArrayOfNumbers)