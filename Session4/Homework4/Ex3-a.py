import random

text = "battleground"

character = list(text)



jumbler=""

while text:
    position = random.randrange(len(text))
    jumbler = jumbler + text[position]
    text = text[:position] + text[(position + 1):]


print("The jumbler is: ", *jumbler, sep=" ")

a = input(("Input your guess: "))

if a == 'battleground':
    print("Excellent - Good job")
else:
    print("Sorry - Have a nice day!")
