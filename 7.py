nonSorted = [8,3,5,1,8,12,4]

for i in range(len(nonSorted)-1):
    for j in range(len(nonSorted)-1):
        if nonSorted[j] > nonSorted[j+1]:
            nonSorted.insert(j+2,nonSorted[j])
            nonSorted.pop(j)
print(nonSorted)




#Bianry search

ListOfElemets = [1,2,4,5,85,100,169,1000,2500,3200,6500]
SearchedNumber = 3


while len(ListOfElemets) > 1:
    Pivot = len(ListOfElemets) //2
    Length = len(ListOfElemets)
    if SearchedNumber < ListOfElemets[Pivot]:
        ListOfElemets = ListOfElemets[0:Pivot]
    elif SearchedNumber > ListOfElemets[Pivot]:
        ListOfElemets = ListOfElemets[Pivot:Length]
    else:
        print("Number is in the list")
        break
if len(ListOfElemets) == 1:
    if ListOfElemets[0] == SearchedNumber:
        print("Number is in the list")
    else:
        print("Number is not in the list")