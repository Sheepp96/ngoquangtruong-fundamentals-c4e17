import random

WORDS = ['Espresso', 'Americano', 'Latte', 'Cappuccino', 'Mocha', 'Macchiato']

print("---------Welcome to Word Jumble!---------")

play = input("Do you wanna play? (yes or no): ")


while play == 'yes':

    word = random.choice(WORDS)
    correct = word
    jumble = ""

    while word:
        position = random.randrange(len(word))
        jumble = jumble + word[position]
        word = word[:position] + word[(position + 1):]

    print("And here the jumble: ", *jumble, sep = " ")

    a = input("And your guess is: ")

    if a == correct:
        print("Excellent - Good job!")

    else:
        print("Sorry - Have a nice day!")

    play = input("Do you wanna play again? ")

print("---Have a nice day!---")
