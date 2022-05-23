pole = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [10,4,82,47,65]
    ]

index = 0
heighth = 0
maxValue = 0
resuts = []
def Look(index,heighth,value):
    global resuts
    if heighth < len(pole) -1:
        Look(index,heighth +1, value + pole[heighth+1][index])
        Look(index+1,heighth +1, value + pole[heighth+1][index+1])
    else:
        resuts.append(value)
Look(0,0,pole[0][0])
print(max(resuts))