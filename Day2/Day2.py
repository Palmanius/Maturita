with open("Day2\Day2.txt","r") as f:
    Course = []
    for line in f:
        Course.append(line.strip().split(" "))
x = 0
y = 0
for line in Course:
    if line[0] == "forward":
        x += int(line[1])
    elif line[0] == "up":
        y -= int(line[1])
    else:
        y += int(line[1])

print(x*y)