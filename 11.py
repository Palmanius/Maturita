from random import shuffle
from math import factorial
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

Possible = []


while len(Possible) < factorial(len(vowels)):
    shuffle(vowels)
    Word = ""
    for letter in vowels:
        Word+= letter
    if Word not in Possible:
        Possible.append(Word)
print(Possible,len(Possible))

solutions = []
def permute(path, remaining):
    if len(remaining) == 0:
        solutions.append(path)
    else:
        for i in remaining:
            r = [x for x in remaining if x != i]
            permute(path+i, r)
permute("", vowels)
print(solutions, len(solutions))