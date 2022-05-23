from tracemalloc import start


Start = 2*3*5*7*11*13*17*19*23*29*30
number = Start
done = False
while not done:
    done = True
    for i in range(2,31):
        if number % i != 0:
            done = False
    if not done:
        number += Start
print(number)