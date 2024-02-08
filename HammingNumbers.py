Hamming = []
Number = 500
# Hamm = 2^i * 3^j * 5^k
# i,j,k >=0

def HammNum(i,j,k):
    global Hamming, Number
    Num = (2**i)*(3**j)*(5**k)

    if Num <= Number:
        if Num not in Hamming:
            Hamming.append(Num)
        HammNum(i+1,j,k)
        HammNum(i,j+1,k)
        HammNum(i,j,k+1)
HammNum(0,0,0)

print(sorted(Hamming))
#1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27