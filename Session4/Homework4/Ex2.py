from random import *

print("-----Guess your number game-----")
input("Now you think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")

print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' if my guess if 'L'arger than your number")

loop = True

while loop:

    n = randint(0,100)
    print("Is ", n, "your number?", end =" ")
    input(str(a))

    if a == 'c':
        print("Hura - I did it")
    elif a == 's':
        
    elif a == 'l':
