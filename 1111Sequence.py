Sequence = [1,1,1,1]


N = 30

for i in range(N-4):
    Sequence.append(sum(Sequence))
    Sequence.pop(0)

print(Sequence)