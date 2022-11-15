with open("trash.txt","r",encoding="utf") as f:
    thing = []
    for line in f:
        if line[0:5] == "alias":
            thing.append(line.strip().split(" "))

counter = 0

for index,line in enumerate(thing):
    thing[index][1] = "\"trashtalker"+str(counter)+"\""
    thing[index][len(thing[index])-1] = "trashtalker"+str(counter+1)+"\""
    counter += 1

with open("NewTrash.txt","w",encoding="utf") as f:
    for line in thing:
        newSTR = ""
        for part in line:
            newSTR += part+" "
        f.write(newSTR + "\n")