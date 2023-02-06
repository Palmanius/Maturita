from random import shuffle
Value = 54125
Notes = {
    500:0,
    200:0,
    100:0,
    50:0,
    20:0,
    10:0,
    5:0,
    2:0,
    1:0
}

for option in Notes:
    Notes[option] += Value // option
    Value = Value % option
print(Notes)

#task3

vowels = ["a","e","i","o","u"]
vowels2 = vowels.pop(0)
Possible = []
Done = False
while not Done:
    Done = True
    for i in range(100000):
        shuffle(vowels)
        Word = ""
        for letter in vowels:
            Word+= letter
        if Word not in Possible:
            Possible.append(Word)
            Done = False
print(Possible)