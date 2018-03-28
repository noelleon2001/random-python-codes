# Question 3 Numeric Scores program
# Programmer: Leon Chung -- Date: September 27, 2016

# The Problem:
"""
Write a pseudo code algorithm which inputs numeric scores and outputs the average score.
The end of the data is signalled by a user input of -1.
"""

# Pseudo code
"""
count = 0
score = 0
total = 0
WHILE score > -1
    OUTPUT "Input a score: "
    score = USERINPUT
    total = total + score
    count = count + 1
ENDWHILE
average = total/count
OUTPUT ("The average is "+average)

"""

# Program

# Welcome text
print("Welcome to the Numeric Score counter!!!")
print("Input -1 to end data!")

# Calculations
count = 0
score = 0
total = 0
while score > -1:
    score = int(input("\nEnter a score: "))
    total += score
    count += 1
average = (total+1) / (count-1)
print("The average is {0}".format(average))

# Exit
input("Press ENTER to exit")

