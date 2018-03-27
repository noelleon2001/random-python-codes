# Made by: Leon Chung
import time
import random
print("\t\t\t --- Hangman Game ---")
name = input("What is your name? ")
name= name.title()
print ("\nHello, " + name )
input("Press ENTER to play hangman!")
print ("\nStarting game...")
time.sleep(1)
n= random.randint(1,4)
if n==1 :
    word = "secret"
elif n==2:
    word= "computer"
elif n==3:
    word="science"
elif n== 4:
    word="hangman"
number= len(word)
print("Hint: This word has {0} characters!".format(number))
guessing = ''
turns = 10
tries=0
while turns > 0:
    failed = 0
    for character in word:
        if character in guessing:
            print (character),
        else:
            print ("_"),
            failed += 1
    if failed == 0:
        print ("\nCongrats, you WON!")
        print("You have {0} incorrect guesses".format(tries))
        break

    guess = input("\nGuess a character:")
    guessing+=guess
    if guess not in word:
        tries += 1
        turns -= 1
        print ("Incorrect")
        print ("You have", + turns, 'more guesses')

        if turns == 0:
            print ("\nSorry, you FAILED!")
            print("The word is: " + word)
input("Press ENTER to exit")
