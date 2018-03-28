# Question 3 Throwing Dice program
# Programmer: Leon Chung -- Date: September 30, 2016

# The Problem:
"""
Write pseudo code for a program which simulate throwing
two dice and then outputs the number on each die
and the total of the two dice.
"""

# Pseudo code
"""
IMPORT random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
OUTPUT (dice1)
OUTPUT (dice2)
OUTPUT (total)
"""

# Program
import random

# Welcome text
print("Welcome to Star Drawing program")

# Calculations
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
print ("\nThe number on first dice is {0} and the second dice is {1}".format(dice1,dice2))
print ("\nThe total is {0}".format(total))

# Exit
input("Press ENTER to exit")


