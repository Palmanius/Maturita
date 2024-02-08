N = 5
for i in range(N,0,-1):
    #print("*"*i)
    pass

for i in range(N):
    line = (N-i)*"." + "*."*i + "*" + (N-i)*"." 
    print(line)

d1 = {123: 3, 124: 4}
d2 = {123: 3, 124: 4}
if d1 == d2:
    print("yes")