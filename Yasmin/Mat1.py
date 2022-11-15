print("We are solving quadratic equation in the following form:\n")
print("𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0")
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

D =b**2  -4*a*c

if D < 0 :
    print("No solution.")
elif D == 0:
    print("X = "+ str(-b / 2*a))
else:
    print("X1 ="+ str((-b + D**0.5) /2*a) + " X2= " + str((-b - D**0.5) /2*a))
