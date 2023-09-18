with open("Day1\Day1.txt","r") as f:
    listofNum = []
    for line in f:
        listofNum.append(int(line))

print(len([i for i in range(len(listofNum)-1) if listofNum[i]<listofNum[i+1]]))

result = 0

for i in range(0,len(listofNum)-1):
    if listofNum[i] < listofNum[i+1]:
        result+=1
print(result)

