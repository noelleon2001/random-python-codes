# Question 2 Counter Check-out program
# Programmer: Leon Chung -- Date: September 5, 2016

# The Problem:
"""
Write pseudo code for a program which ask a multiple choice quiz question,e.g. “What is the world’s largest ocean?”.
It then gives 3 possibilities numbered 1, 2 and 3 and asks the user to enter 1, 2 or 3.
An appropriate response is then output.
"""

# Pseudo code
"""
OUTPUT "What is the world’s largest ocean?"
OUTPUT "1. Atlantic"
OUTPUT "2. Pacific"
OUTPUT "3. Indian"
answer = USERINPUT
IF answer = 2 THEN
    OUTPUT "Correct"
ELSE
    OUTPUT "Wrong, the correct answer is Pacific"
ENDIF
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


