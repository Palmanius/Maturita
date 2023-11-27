def Power(n,p):
    if p == 0:
        return(1)
    if p == 1:
        return(n)
    return n * Power(n,p-1)



number = 3
power = 4
print(Power(number,power))

