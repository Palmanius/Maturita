# Q05

# Array of words
wordArray = ["wind","leer","pushy","lade","size","sob","borrowing","list",
             "perish","hoax","sticks","seed","impel","large","male","silent",
             "quilt","sobbed","remarkable","fantastic","wire","reflective","putrid", 
             "pushover","swing"]


# Add your code here

word = input("Enter a word or 1 to exit: ")
print("------------------------------------")

while word != "1":
    sameLetter = []
    wordIn = []
    for i in wordArray:
        if word[0] == i[0]: #condition for first letter
            sameLetter.append(i)
        if word in i: #condition for word in word
            wordIn.append(i)
    
    short = word[0]
    long = ""
    for i in wordIn:
        if len(i) < len(short): #condition for shortest word in wordIn
            short = i
        if len(i) > len(long): #condition for longest word in wordIn
            long = i

    #printing of Same letter words
    print(*sameLetter, sep = "\n")
    print("\n", len(sameLetter), " word(s) begin with ", word[0],"\n------------------------------------", sep="")

    #printing of words that include word
    print(*wordIn, sep = "\n")
    print("\n", len(wordIn), " word(s) begin with ", word,sep="")

    #printing longest and shortest words and their lengths
    print("The longest word has",len(long), "leters")
    print("The shortest word has",len(short), "letters")
    print("The longest word is", long)
    print("The shortest word is ", short, "\n------------------------------------", sep="")

    word = input("Enter a word or 1 to exit: ") #condition to stop/continue while loop