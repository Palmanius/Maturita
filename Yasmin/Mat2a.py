print("Give me two numbers to find HCD")
a = int(input("Number 1 = "))
b = int(input("Number 2 = "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)