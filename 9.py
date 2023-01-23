#BinToDen
Bin = "101011101"
RunningSum = 0
Exp = 1
for n in reversed(Bin):
    if n == "1":
        RunningSum += Exp
    Exp *= 2
print(RunningSum)


#SumTwoBin

Bin1 = "11010101"
Bin2 = "10100100"
CarryOver = 0
NewBin = ""

for i in range(len(Bin1)-1,-1,-1):
    Result = int(Bin1[i]) + int(Bin2[i]) + CarryOver
    if Result == 0:
        NewBin = "0" + NewBin
    elif Result == 1:
        NewBin = "1" + NewBin
        CarryOver = 0
    elif Result == 2:
        NewBin = "0" + NewBin
        CarryOver = 1
    else:
        NewBin = "1" + NewBin
        CarryOver = 1

if CarryOver == 1:
    NewBin = "1" + NewBin
print(NewBin)