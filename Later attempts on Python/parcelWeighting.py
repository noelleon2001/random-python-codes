# Question 3 Parcel cost program
# Programmer: Leon Chung -- Date: September 8, 2016

# The Problem:
"""
The cost of posting a small parcel of up to 1kg is is £4.40.
The cost for a parcel weighing more than 1kg, but less than or equal to 2kg, is £6.55.
Draw a flowchart to allow the user to input the weight of the parcel and calculate and output the cost of postage.
If the user enters a weight greater than 2kg, display a message “This is not a small parcel” and end the program.
Write the equivalent pseudo code for this algorithm.
"""

# Pseudo code
"""
OUTPUT "What is the weight of parcel?"
weight = USERINPUT
IF weight <= 0 THEN
    OUTPUT "Value is incorrect"
ELSE weight = 1 THEN
    OUTPUT "The cost is £4.40"
ELSE weight <= 2 THEN
    OUTPUT "The cost is £6.55"
ELSE
    OUTPUT "This is not a small parcel"
ENDIF
"""

# Program

# Welcome text
print("Welcome to the Parcel Costing program!!!")

# Question
print("\nWhat is the weight of the parcel?")

# Calculations
weight = float(input("Weight = "))
if weight <= 0:
    print ("\nValue is incorrect")
elif weight <= 1:
    print ("\nThe cost of parcel is £4.40")
elif weight <= 2:
    print ("\nThe cost of parcel is £6.55")
else:
    print ("\nThis is not a small parcel")

# Exit
input("\nPress ENTER to exit")

