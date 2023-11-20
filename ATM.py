money = {"1":0,"2":0,"5":0,"10":0,"20":0,"50":0,"100":0,"200":0,"500":0}
value = int(input("What amount of money would you like to pay out?"))

for note in reversed(money.keys()):
    money[note] += value // int(note)
    value %= int(note)
print(money)