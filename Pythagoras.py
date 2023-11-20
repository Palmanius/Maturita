x,y = int(input("Number 1: ")), int(input("Number 2: "))

hyp = input("Is one of your numbers the hypotenuse? (Y/N): ")
if hyp.lower() == "y":
    print("The lenght of the third side is", abs(x**2 - y**2)**0.5)
elif hyp.lower() == "n":
    print("The lenght of the third side is", (x**2 + y**2)**0.5)
else:
    print("invalid input")
