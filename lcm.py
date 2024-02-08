from math import lcm

su = 1
for num in range(1, 31):
    su = lcm(su, num)

x = [(lambda ssum, i: lcm(ssum, i))(1, i) for i in range(1, 31)]

print(x)