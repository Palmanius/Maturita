string = "Never gonna give you up".split(" ")

reversedString = ""
for word in string:
    reversedWord = ""
    for letter in word:
        reversedWord = letter + reversedWord
    reversedString += reversedWord + " "
print(reversedString)