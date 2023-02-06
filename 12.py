# #task2
# A = input("First side of the triangle")
# B = input("Second side of the triangle")
# C = (int(A)**2 + int(B)**2)**(0.5)

# print("Third side of the triangle is: "+str(C))

#task3
from math import factorial
number = str(factorial(25))
counter = 0
for n in reversed(number):
    if n =="0":
        counter += 1
    else:
        break
print(number)
print(counter)




