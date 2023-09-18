firstDay = int(input("Which day does June start with?\n"))
days =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
June = [days]
firstweek = []
day = 1
for i in range(1,firstDay):
    firstweek.append("   ")
for i in range(firstDay,8):
    firstweek.append(" "+str(day)+" ")
    day += 1

June.append(firstweek)
while day < 31:
    nextWeek =[]
    for i in range(7):
        if day > 9 and day < 31:
            nextWeek.append(""+str(day)+" ")
            day += 1
        elif day < 31:
            nextWeek.append(" "+str(day)+" ")
            day += 1
    June.append(nextWeek)


for line in June:
    print(line)