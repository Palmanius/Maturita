Pyramid = []
with open("Pyramyd.txt","r") as f:
    for line in f:
        Pyramid.append([int(x) for x in line.strip().split(",")])

print(Pyramid)

paths = []
def recurse(path):
    if len(path) == len(Pyramid):
        value = 0
        for j, k in enumerate(path):
            value += Pyramid[j][k]
        paths.append(value)
        return

    recurse(path + [path[-1]])
    recurse(path + [path[-1]+1])

recurse([0])
print(max(paths))    