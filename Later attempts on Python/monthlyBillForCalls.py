# Question 1 Monthly Bill for Calls program
# Programmer: Leon Chung -- Date: September 28, 2016

# The Problem:
"""
Write a pseudo code algorithm for computing the monthly bill for calls on a mobile phone.
"""

# Pseudo code
"""
tariff = 23
rate = 0
OUTPUT (What is the minutes used?)
minutesused = USERINPUT
OUTPUT (What is the per minutes rate in £?)
rate = USERINPUT
IF minutesused > 600 THEN
    extra = minutesused - 600
    charge = extra * rate
    OUTPUT (tariff + charge)
ELSE
    OUTPUT (tariff)
"""

# Program

# Welcome text
print("Welcome to the Monthly Bill for Calls!!!")

# Calculations
tariff = 23
minutesused = float(input("\nWhat is the minutes used? "))
rate = float(input("\nWhat is the per minutes rate in £? "))
if minutesused > 600:
    extra = minutesused - 600
    charge = extra * rate
    print ("\nThe total charge is {0}".format(tariff + charge))
else:
    print ("\nThe total charge is {0}".format(tariff))

# Exit
input("\nPress ENTER to exit")

