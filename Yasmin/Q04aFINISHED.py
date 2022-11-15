# Q04a


denaryPlaceholders = [128, 64, 32, 16, 8, 4, 2, 1]
binaryPattern = ""
denaryNumber = 0
count = 0


# Add your code here

bnum = input('Enter a binary 8-bit number: ')
l = len(bnum)

if l > 8: 
    bnum = ValueError
    print (' Number > 8. Enter a 8-bit binary number: ')
    count = 2

elif l < 8:
    bnum = ValueError
    print ('Number < 8. Enter a 8-bit binary number: ')  
    count = 1

if count == 0:
    for x in bnum: 
            l = l - 1                                   #decrease lentgh by 1
            denaryNumber += pow(2, l) * int(x)          #multiply each of the digits with its corresponding value of two according to their placement (l - 1)

print (bnum, denaryNumber)




