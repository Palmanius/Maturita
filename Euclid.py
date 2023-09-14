HCF = 0

a = 120
b = 25

while a!=b:
    if a>b:
        a-=b
    else:
        b-=a

print(a)