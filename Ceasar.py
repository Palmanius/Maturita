par = int(input("Give me a positive integer\n")) % 26
mes = input("Give me a message to encode\n")

newmes = ""
for letter in mes:
    if ord(letter)+par >122:
        newmes += chr(ord(letter) + par - 26)
    elif ord(letter)+par < 97 and ord(letter)+par > 90 :
        newmes += chr(ord(letter) + par - 26)
    elif ord(letter) < 65 or ord(letter) > 122:
        newmes += letter
    else:
        newmes += chr(ord(letter) + par)

print(newmes)

alphabet = ["a","b","c","d","e","f","g","h","i"]
newmes = ""
for letter in mes:
    if letter in alphabet:
        newmes += alphabet[alphabet.index(letter) + par]

