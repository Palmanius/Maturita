with open("reply2024\Cars\input.txt","r") as f:
    Cases = []
    T = int(f.readline())
    for i in range(T):
        Cars = []
        RC = [int(x) for x in f.readline().strip().split(" ")]
        for j in range(RC[1]):
            Cars.append([int(x) for x in (f.readline().strip().split(" "))])
        Cases.append([RC[0]]+Cars)
print(Cases)
with open("reply2024\Cars\output.txt","w") as o:
    for case in Cases:
        for car in case[1:]:
            case[0] 
