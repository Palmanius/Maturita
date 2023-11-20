x = 4617
amount_of_zeros = 0
multiplier = 5
while x >= multiplier:
     amount_of_zeros += x//multiplier
     multiplier*=5
print (amount_of_zeros)