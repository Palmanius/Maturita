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
    for i,case in enumerate(Cases):
        print(case)
        R = case[0]
        winner = [0,10000]
        for car in case[1:]:
            cs = car[1]
            ct = car[2]
            cc = car[3]
            cd = car[4]

            normal = car[1]*car[3]
            turbo = car[2]*car[4]
            loops = R//(normal+turbo)
            rem = R%(normal+turbo)
            time = loops * ((cc + cd))
            
            if rem <= turbo:
                time += rem/ct
            else:
                time += (cd + ((rem - turbo)/cs))
            print(time)
            if time < winner[1]:
                winner[0] = car[0]
                winner[1] = time
        if i!= 0:
            o.write("\n")
        o.write(f"Case #{i+1}: {winner[0]}")