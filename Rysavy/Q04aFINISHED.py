# Q04a

denaryPlaceholders = [128, 64, 32, 16, 8, 4, 2, 1]
binaryPattern = ""
denaryNumber = 0
count = 0

# Add your code here

while len(binaryPattern) != 8:
    binaryPattern = input("Enter 8-bit binary number")

for digit in binaryPattern:
    if digit == "1":
        denaryNumber = denaryNumber + denaryPlaceholders[count] * 1
    count = count + 1

print(binaryPattern, "converted is", denaryNumber)
    