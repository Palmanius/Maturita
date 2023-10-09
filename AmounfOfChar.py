ListOfChar = {}
with open("String.txt","r") as f:
    for line in f:
        for c in line:
            if c.lower() in ListOfChar:
                ListOfChar[c.lower()] += 1
            else:
                ListOfChar[c.lower()] = 1

print(ListOfChar["a"])


            