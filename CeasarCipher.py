LowerCase = "abcdefghijklmnopqrstuvwxyz"
UpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Text = "Never gonna give you up!"
NewText = ""
Key = -2
for c in Text:
    Lower = False
    if c in LowerCase:
        NewText += LowerCase[((LowerCase.index(c) + Key) % len(LowerCase))]
    elif c in UpperCase:
                NewText += UpperCase[((UpperCase.index(c) + Key) % len(UpperCase))]
    else: NewText += c
print(NewText) 
