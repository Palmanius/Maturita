field = [1,8,9,6,5,1,5,8]
count = 0
for i in range(0,len(field)-1):
    if field[i] < field[i+1]:
        count +=1
print(count)
