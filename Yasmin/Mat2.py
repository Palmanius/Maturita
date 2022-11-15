array = [1,2,3,4,5,"6a",7]
sum = 0
for num in array:
    try:
        sum += num
    except:
        print("This is not a number "+ num)
        break
print(sum)