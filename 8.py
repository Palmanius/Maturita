Hex = ""
Bin = "1010111000001010"
Table = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F"
}
modulus = len(Bin) % 4

if modulus != 0:
    Bin = "0"*(4-modulus) +Bin

while len(Bin) >0:
    Hex += Table[Bin[0:4]]
    Bin = Bin[4:]
print(Hex)


#part2
from random import randint
GuessNumber = randint(0,100)
NumberOfGuesses = 1
while True:
    GuessedNumber = int(input("Guess a number between 0 and 100\n"))
    if GuessedNumber > GuessNumber:
        print("Your guess is too high")
    elif GuessedNumber < GuessNumber:
        print("Your guess is too low")
    else:
        break
    NumberOfGuesses += 1
print("You have guessed the number "+str(GuessNumber)+" in "+str(NumberOfGuesses)+" times.")