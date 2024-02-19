with open("Pyramyd.txt","r") as f:
    Pyramid = []
    for line in f:
        Pyramid.append([int(x) for x in line.strip().split(",")])

def FindPath(index,depth,value):
    if depth == len(Pyramid)-1:
        return(value)
    return max([FindPath(index,depth+1,value+Pyramid[depth+1][index+1]),FindPath(index+1,depth+1,value+Pyramid[depth+1][index+1])])

print(FindPath(0,0,Pyramid[0][0]))    