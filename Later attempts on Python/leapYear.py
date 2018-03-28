# Question 3 Leap year program
# Programmer: Leon Chung -- Date: September 13, 2016

# The Problem:
"""
Write pseudo code for one or more selection statements to decide whether a year is a Leap year. The rules are:
A year is generally a Leap Year if it is divisible by 4, except that if the year is divisible by 100,
it is not a Leap year, unless it is also divisible by 400. Thus 1900 was not a Leap Year, but 2000 was a Leap year.
"""

# Pseudo code
"""
OUTPUT "Enter the year:"
year = USERINPUT
leapyear = FALSE
IF (mod(year,4) = 0) THEN
    leapyear = TRUE
IF (mod(year,100) = 0) THEN
    leapyear = FALSE
IF (mod(year,400) = 0) THEN
    leapyear = TRUE
IF leapyear = TRUE THEN
    OUTPUT "It is a leap year"
ELSE
    OUTPUT "It is not a leap year"
"""

# Program

# Welcome text
print("Welcome to the Leap Year program!!!")

# Question
year = int(input("\nEnter the year:"))

# Calculations
leapyear = False
if year % 4 == 0:
    leapyear = True
if year % 100 == 0:
    leapyear = False
if year % 400 == 0:
    leapyear = True


if leapyear == True:
    print("It is a leap year")
else:
    print("It is not a leap year")

# Exit
input("\nPress ENTER to exit")

