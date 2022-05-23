n = int(input("Give n \n"))

divisors = 1
x = 1
number = 1
while divisors < n:
    x +=1
    number += x
    newdiv = 2
    for i in range(2,(number//2) +1):
        if number % i == 0:
            newdiv += 1
    divisors = newdiv

print(number)