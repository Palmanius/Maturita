Binary = "111101011"
Hexa = ""
ConversionTable = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F"
}
if len(Binary)%4 != 0: Binary = "0"*(4-len(Binary)%4) + Binary
for i in range(0,len(Binary),4):
    print(Binary[i:i+4])
    Hexa += ConversionTable[Binary[i:i+4]]
print(Hexa)

print(str(hex(int(Binary,base=2))))