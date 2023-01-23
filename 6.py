from random import *
import math
import pygame

ranNum = randint(0,60)
print(ranNum)

nonSorted = ["Book","Pencil","Yes","No","Maybe","Perhaps","Chance"]
Sorted = []

for UnsortedNum in nonSorted:
    if len(Sorted) == 0:
        Sorted.append(UnsortedNum)
    elif UnsortedNum >= max(Sorted):
        Sorted.append(UnsortedNum)
    else:
        for pos,SortedNum in enumerate(Sorted):
            if UnsortedNum < SortedNum:
                Sorted.insert(pos,UnsortedNum)
                break
print(Sorted)   

Word = "Splendid"
letter = "d"
Count = 0
for c in Word:
    if c == letter:
        Count+=1
print(Count)

print(Word.count("d"))