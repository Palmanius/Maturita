import math
A = 16
if math.log2(A).is_integer():
    print("It is power of two")
else:
    print("It is not")
print(math.log2(A))