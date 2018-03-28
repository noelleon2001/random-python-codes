# Question 3 Temperature program
# Programmer: Leon Chung -- Date: September 19, 2016

# The Problem:
"""
Write a pseudo code algorithm which asks a user to enter a number between 5 and 20.
If they enter a number outside this range,
the program asks them repeatedly to re-enter the number until they enter a valid number.
"""

# Pseudo code
"""
n = 0
total = 0
WHILE n <= 5 and n >= 20
    OUTPUT "Please enter a valid number: "
    n = USERINPUT
ENDWHILE
FOR temp IN (0,n) THEN
    OUTPUT "Enter temperature: "
    temp = USERINPUT
    total += temp
average = total / n
OUTPUT (average)
"""

# Program

# Welcome text
print("Welcome to the Temperature Program!!!")

# Calculations
total = 0
num = False
while num == False:
    n = int(input("Please enter a valid number between 5 and 20: "))
    if n < 5 and n > 20:
        num = False
    else:
        num = True
for temp in range(0,n):
    temp = int(input("Enter temperature: "))
    total += temp
average = total / n
print("\nThe average temperature is {0}".format(average))

# Exit
input("Press ENTER to exit")


