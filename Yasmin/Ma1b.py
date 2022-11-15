SET = [1,2,3,4,5,6,7,8,9]
NEWSET = []
NEWSET.append(SET[len(SET)-1])
for i in range(0,len(SET)-1):
    NEWSET.append(SET[i])
print(NEWSET)