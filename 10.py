# from random import randint
# while True:
#     Num1 = randint(0,10)
#     Num2 = randint(0,10)
#     Result = Num1*Num2
#     if input("What is "+str(Num1) +" * "+str(Num2)+" equal to?\n") == str(Result):
#         print("Correct answer!")
#     else:
#        print("Incorrect, it is "+str(Result))

Num1 = int(input("Gib first number"))
Num2 = int(input("Gib full number"))

A = Num1
B = Num2
while Num1 != Num2:
    if Num1 < Num2:
        Num1 += A
    else:
        Num2 += B
print(Num1)