from math import sqrt

print("We are solving a quadratic equation in a form y = a*x^2 + b*x +c \n")
a = int(input("Value of a = "))
b = int(input("Value of b = "))
c = int(input("Value of c = "))

D = b*b - 4*a*c

if D <0:
    print("Equation has no solution.\n")
elif D == 0:
    print("y= " + str(-b/(2*a)))
else:
    Square = sqrt(D)
    print("y1= " +str((-b +Square)/(2*a)))
    print("y2= " +str((-b -Square)/(2*a)))