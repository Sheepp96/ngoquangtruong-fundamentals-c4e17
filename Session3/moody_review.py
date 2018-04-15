from random import randint

n = randint(0, 100)

if n < 30:
    print("I feel sad :'( ")
    print(n)
elif n <60:
    print("I feel normal")
    print(n)
else:
    print("Oh yeah")
    print(n)
