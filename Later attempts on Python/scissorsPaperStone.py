# Question 5 Scissors, paper, stone program
# Programmer: Leon Chung -- Date: September 8, 2016

# The Problem:
"""
Nazim wants to create a game of scissors, paper, stone.
In this game two people simultaneously make their hand into a shape representing scissors, paper or stone. Scissors cuts paper, so wins.
Paper wraps stone, so wins.  Stone breaks scissors, so wins.
Nazim starts by generating 2 random numbers between 1 and 3 to represent the three possibilities, and assigning them to scissors (1), paper (2) or stone (3).
"""

# Pseudo code
"""
Hand1 = random(1,3)
    Hand2 = Random(1,3)
    Case Hand1 of
        1: Player1 = “Scissors”
        2: Player1 = “Paper”
        3: Player1 = “Stone”
    End Case
    Case Hand2 of
        1: Player2 = “Scissors”
        2: Player2 = “Paper”
        3: Player2 = “Stone”
    End Case
    IF Player1 = “Scissors” THEN
        Case Player2 of


"""

# Program

# Welcome text
print("Welcome to the Ocean Quiz!!!")

# Question
print("\nWhat is the world’s largest ocean?")
print("1. Atlantic\n2. Pacific\n3. Indian")

# Calculations
answer = int(input("Answer ="))
if answer == 2:
    print("Correct")
else:
    print("Wrong, the correct answer is Pacific")

# Exit
input("Press ENTER to exit")

