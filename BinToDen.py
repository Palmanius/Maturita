Bin = "10010"

def BinToDen(Bin):
    expo = 1
    Den = 0
    for bit in Bin[::-1]:
        if bit == "1":
            Den += expo
        expo *= 2
    return Den



print(int(Bin,2))
print(BinToDen(Bin))
