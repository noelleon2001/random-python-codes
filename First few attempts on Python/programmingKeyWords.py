# Programmer: Leon
import random

print("\t\t\t???Programming Keywords Quiz???")
input("Press ENTER to play:")
play = True
while play==True:
    word ={ "Base-2 number system" : "binary",
            "7-bit text encoding standard" : "ascii",
            "8 bits" : "byte",
            "1024 bytes" : "kilobyte",
            "A series of steps to solve a problem or carry out a task" : "algorithm",
            "A continuously changing wave, such as natural sound" : "analogue",
            "First generation programming language" : "machine code",
            "Second generation programming language" : "assembly code",
            "Third generation programming language" : "high level language",
            "Fourth generation programming language" : "sql"}
    score = 0
    num = int(input("\nHow many questions would you like to do: "))
    for number in range(num):
        question = (random.choice(list(word.keys())))
        answer = word[question]
        print("\nQuestion " + str(number+1) )
        guess=input("What is " +question.lower()+ "?")
        if guess.lower() == answer:
            print("Correct!")
            score += 1
            del word[question]
        else:
            print("Incorrect!")
            print("The correct answer is "+answer)
        if score==10:
            print("You answered all the questions correctly!")
            break
    print("\nYour score is " + str(score))
    replay = input("Press ENTER to play again or enter 'n' to quit")
    if replay.lower() == 'n':
        playing = False
        break