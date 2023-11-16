from random import randint
while True:
    a = randint(0,10)
    b = randint(0,10)
    try:
        if int(input(f"What is {a} multiplied by {b}?\n")) == a*b:
            print(f"That is correct! {a} multiplied by {b} is {a*b}\n")
        else:
            print(f"That is not correct! {a} multiplied by {b} is {a*b}\n")
    except: break