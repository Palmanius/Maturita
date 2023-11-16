def AddBinary(Bin1,Bin2):

    CarryOver = 0
    Result = ""

    #make both numbers equally long by adding zeroes to the front of shorter ones
    if len(Bin1) > len(Bin2):
        Bin2 = "0"*(len(Bin1)-len(Bin2)) + Bin2
    else: Bin1 = "0"*(len(Bin2)-len(Bin1)) + Bin1
#resolve for each possible option of adding Bin1, Bin2 and carryover
    for i in range(len(Bin1)-1,-1,-1):
        Mid = int(Bin1[i]) + int(Bin2[i]) + CarryOver
        if Mid == 3:
            Result = "1" + Result
        elif Mid == 2:
            CarryOver = 1
            Result = "0" + Result
        elif Mid == 1:
            CarryOver = 0
            Result = "1" + Result
        else:
            CarryOver = 0
            Result = "0" + Result
#Resolve overflow problem
    if CarryOver == 1:
        Result = "1" + Result
    return Result


print(AddBinary("1011","1001"))

Bin1 = "1011"
Bin2 = "1001"

print(bin((int(Bin1,2)+int(Bin2,2)))[2:])