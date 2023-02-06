Fibb = [1,1]
index = 2
while len(str(Fibb[1])) < 500:
    Fibb.append(sum(Fibb))
    Fibb.pop(0)
    index+=1
print(index,Fibb[1])

#task3

String = "Never gonna give you up!"
Count = String.count(" ")
String = String.replace(" ","")
String = " "*Count + String
print(String)