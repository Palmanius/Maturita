ar = [1,2,3,4,5,6,7,8]
average = sum(ar) // len(ar)
deviate = [0,0]
for num in ar:
    if abs(average-num) > deviate[1]:
        deviate[0] = num
        deviate[1] = abs(average-num)
print(deviate)


def replacespaces(sentance):
    print(sentance.replace(" ","*"))

replacespaces("Never gonna give you up!")