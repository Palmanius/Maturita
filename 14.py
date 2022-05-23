digits = ["0","1","2","3","4","5","6","7","8","9"]
phoneNumber = input("Give me a phone numbers.\n")
for dig in phoneNumber:
    if dig in digits:
        digits.remove(dig)
print("Your number is missing the following digits:",digits)