# Q02a

numberList = [5, 9, 13, 63, 65, 79, 86, 100]
start = 0
middle = 0
end = len(numberList) - 1
found = False
count = 0

# Add your code here

item = int(input("Please enter the number to find"))
while start <= end and not found:
    middle = (start + end) // 2
    if numberList[middle] == item:
        found = True
    else:
        if item < numberList[middle]:
            end = middle - 1
        else:
            start = middle + 1
    count = count + 1






# Do not add your own code below this line
    
# Result of the search is displayed (this has been done for you)

if found == True:
    print("item" , "was found in the list")
else:
    print("item" , "is not in the list")
