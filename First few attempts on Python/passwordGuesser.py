# Programmer: Leon
import random

print ('\t\t\t\t\t ^^^^ Welcome to the Password Guesser game ^^^^')
input("Press ENTER to start the game.")
name=input("\nPlease enter your name: ")
n = 1
to_be_guessed = int(n * random.randint(1, 10))
guess = 0
i=0

while i < 10:
    guess = int(input("Guess a positive number: "))
    i += 1
    if guess > to_be_guessed:
            print("Number too large")
    elif guess < to_be_guessed:
            print("Number too small")
    if guess== to_be_guessed:
        print("Congratulation. You made it!")
        print("You have tried {0} attempts".format(i))
        break

else:
    print("Sorry, too many attempts!")
    print("You have tried {0} attempts".format(i))




