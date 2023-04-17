a = 1
b = 2
c = 3
d = 4

e = 5
f = 6
g = 7
h = 8
i = 9

def Matrix2(a,b,c,d):
    return(a*d-b*c)

def Matrix3(a,b,c,d,e,f,g,h,i):
    return a * Matrix2(e,f,h,i) -b*Matrix2(d,f,g,i) +c*Matrix2(d,e,g,h)

print(str(Matrix3(a,b,c,d,e,f,g,h,i)))
    