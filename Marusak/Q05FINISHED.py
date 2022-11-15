# Q05

# Array of words
wordArray = ["wind","leer","pushy","lade","size","sob","borrowing","list",
             "perish","hoax","sticks","seed","impel","large","male","silent",
             "quilt","sobbed","remarkable","fantastic","wire","reflective","putrid", 
             "pushover","swing"]


# Add your code here

shortest = 5000
longest = 0
shortestWord = ""
longestWord = ""

inputWord = input("Enter a Word or 1 to exit: ")

if inputWord != "1":
    count = 0
    for word in wordArray:
        if word[0] == inputWord[0]:
            print(word)
            count = count + 1
print("\n",count,"Word(s) Beggining With",inputWord[0])

count = 0

for word in wordArray:
    if inputWord in word:
        count = count + 1
        print(word)
        length = len(word)
        if longest < length:
            longest = length
            longestWord = word
        if shortest > length:
            shortest = length
            shortestWord = word

if count > 0:
    print(count, "Word(s) with", inputWord, "In them")
    print("The longest word has", longest, "Letters")
    print("The shortest word has", shortest, "Letters")
    print("The lonest word is", longestWord)
    print("The shortest word is", shortestWord)
else:
    print("There were 0 words with all the letters from", inputWord, "In them")
    print("END OF PROGRAM")