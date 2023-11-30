#Write a program to print the number of prime numbers which are 
#less than or equal to a given integer. 

N = 50000
Solutions = []
if N>2:
    Solutions.append(2)
for i in range(3,N,2):
    IsPrime = True
    for j in range(3,i//2,2):
        if i%j == 0:
            IsPrime = False
            break
    if IsPrime: Solutions.append(i)

print(Solutions)

            


