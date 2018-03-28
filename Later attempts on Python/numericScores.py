# Question 2 Numeric Scores program
# Programmer: Leon Chung -- Date: September 14, 2016

# The Problem:
"""
Write a pseudo code algorithm which inputs numeric scores and outputs how many of them are over 100.
The end of the data is signalled by a user input of -1.
"""

# Pseudo code
"""
count = 0
score = 0
WHILE score > -1
    OUTPUT "Input a score: "
    score = USERINPUT
    IF score >= 100 THEN
        count = count + 1
ENDWHILE
OUTPUT ("The numbers over 100 are "+count)

"""

# Program

# Welcome text
print("Welcome to the Numeric Score counter!!!")
print("Input -1 to end data!")

# Calculations
count = 0
score = 0
while score > -1:
    score = int(input("\nEnter a score: "))
    if score >= 100:
        count += 1
print("The numbers over 100 are {0}".format(count))

# Exit
input("Press ENTER to exit")

