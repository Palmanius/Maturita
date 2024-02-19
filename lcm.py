from math import lcm

su = 1
for num in range(1, 31):
    su = lcm(su, num)

ssum = 1
x = [(lambda ssum, i: lcm(ssum, i))(ssum, i) for i in range(1, 31)]

print(x)