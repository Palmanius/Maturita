from random import randint
Digits = []
for i in range(8):
    Digits.append(randint(0,9))

MinNum = sorted(Digits)
MaxNum = sorted(Digits,reverse=True)

Min = ""
for i in MinNum:
    Min+= str(i)
Max = ""
for i in MaxNum:
    Max += str(i)
print(MinNum,MaxNum)
print(int(Max) - int(Min))

