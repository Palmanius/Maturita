f = open("Day1\D.txt","r")
array = [x for x in f.readlines()]
f.close()

print(array)


a = [1,2,3,4,5,48,1,641,6,163,46]

with open("Day1\output.txt","w") as f:
    for line in a:
        f.write(f"{str(line)}\n")
