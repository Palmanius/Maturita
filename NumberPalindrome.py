#Write a program to reverse the digits of a given number and add it to the original, 
#If the sum is not a palindrome repeat this procedure. 

Number = 696969

while True:
    ReversedNumber = int(str(Number)[::-1])
    Number+=ReversedNumber
    if str(Number) == str(Number)[::-1]:
        break
print(Number)