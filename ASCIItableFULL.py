i = 0
Symbols = []
while True:
    if i <= 55295:
        try: 
            Symbols.append(chr(i))
            i += 1
        except:
            break
    else: break
print(chr(600000))
print(Symbols)
