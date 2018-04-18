from random import *

n = randint(0, 100)
b = 0
loop = True
while loop:

    a = int(input("Guess my number: "))

    if a < n:
        print("Too small")
        b += 1
    elif a > n:
        print("Too big")
        b += 1
    else:
        print("Bingo")
        loop = False

    if b == 8:
        print("Error too many times")
        print("------GAME OVER------")
        loop = False
