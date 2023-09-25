with open("Numbers.txt","r") as f:
    Numbers = []
    for line in f:
        Numbers.append(int(line))

    Average = sum(Numbers) / len(Numbers)

    Numbers.sort()
    if Average - Numbers[0] > Numbers[len(Numbers)-1] - Average:
        print(Numbers[0])
    else:
        print(Numbers[len(Numbers)-1]) 



Sent = "never gonna give you up"
Sent = Sent.replace(" ","*")
print(Sent)