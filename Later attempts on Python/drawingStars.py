# Question 1 Drawing Stars program
# Programmer: Leon Chung -- Date: September 23, 2016

# The Problem:
"""
Write pseudo code for a program which ask a multiple choice quiz question,e.g. “What is the world’s largest ocean?”.
It then gives 3 possibilities numbered 1, 2 and 3 and asks the user to enter 1, 2 or 3.
An appropriate response is then output.
"""

# Pseudo code
"""
star = 0
WHILE star <5 THEN
    line = "*" +(star * "**")
    OUTPUT line
    star += 1
"""

# Program
# Welcome text
print("Welcome to Star Drawing program")

# Calculations
star = 0
while star <5:
    line = "*" +(star * "**")
    print(line)
    star += 1

# Exit
input("Press ENTER to exit")


