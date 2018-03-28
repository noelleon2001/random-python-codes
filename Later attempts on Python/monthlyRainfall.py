# Question 3 Monthly Rainfall program
# Programmer: Leon Chung -- Date: September 30, 2016
# The Problem:
"""
Write pseudo code for inputting the data in Julie’s program,prompting the user with statements such as
“Enter rainfall for January”, “Enter rainfall for February”, etc.,
and then prints the data in a list.
"""
# Pseudo code
"""
OUTPUT ("Welcome to Monthly Rainfall program")
total = 0
above = 0
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
rainfall = [0,0,0,0,0,0,0,0,0,0,0,0]
anualRainfall = 0
FOR number IN range (0,12) THEN
    rainfall[number]=float(input("Input temperature for {0}: ".format(months[number])))
    total += rainfall[number]
average = total / 12
round = round(average, 1)
FOR number IN range (0,12) THEN
    IF rainfall[number] > average THEN
        above += 1
OUTPUT ("The total annual rainfall is "+ str(total))
OUTPUT ("The monthly average rounded is "+ str(round))
OUTPUT ("The number of months that have rainfall above the average value is "+ str(above))
"""
# Program
# Welcome text
print("Welcome to Monthly Rainfall program")
# Calculations
total = 0
above = 0
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
rainfall = [0,0,0,0,0,0,0,0,0,0,0,0]
anualRainfall = 0
for number in range (0,12):
    rainfall[number]=float(input("Input temperature for {0}: ".format(months[number])))
    total += rainfall[number]
average = total / 12
round = round(average, 1)
for number in range (0,12):
    if rainfall[number] > average:
        above += 1
print("\nThe total annual rainfall is "+ str(total))
print("The monthly average rounded is "+ str(round))
print("The number of months that have rainfall above the average value is "+ str(above))
# Exit
input("Press ENTER to exit")

