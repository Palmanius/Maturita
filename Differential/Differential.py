import math

x0 = 0.0
y0 = 1.0
h = 0.1
n = 10

def f(x,y):
    return(2 - ((math.e)**(-4*x)) - (2*y))
def exact(x,y):
    return(1 + (0.5*(math.e)**(-4*x)) - 0.5*(math.e)**(-2*x))
def rou(val):
    divider = 100
    val *= divider
    temp = round(val)
    return temp / divider


def Calculate(x0,y0,h,n):
    x = x0
    y = y0
    for i in range(1,n):
        k = f(x,y)
        y += h*k
        x += h
        print(str(rou(x)) + "\t\t" + str(rou(y)) + "\t\t" + str(rou(exact(x,0))))

Calculate(x0,y0,h,n)