# Question 2 Online Book Store program
# Programmer: Leon Chung -- Date: September 10, 2016
# The Problem:
"""
Write pseudo code for an algorithm which allows the user to enter the total value of their order.
They are then asked whether they want to pay for guaranteed next day delivery.
Depending on their answer, and the value of the order, the program displays the postage charge and the overall total charge.
"""
# Pseudo code
"""
OUTPUT "Enter order value: "
ordervalue = USERINPUT
postcost = 0
OUTPUT "Do you want to pay £5.00 for next day delivery?"
OUTPUT "Enter 1 for next day delivery, 2 for 2nd class delivery"
postcode = USERINPUT
IF ordervalue <= 0 THEN
    OUTPUT "Invalid value"
    ordervalue = 0
ELSE ordervalue >= 15 and postcode == 1 THEN
    postcost = 0
ELSE ordervalue <=15 and postcode == 1 THEN
    postcost = 3.5
ELSE postcode == 2 THEN
    postcost = 5
cost = ordervalue + postcost
OUTPUT (The postage charge is +postcost)
OUTPUT (The total charge is +cost)
"""
# Program
# Welcome text
print("Welcome to the Online BOOK Store!!!")
# Question
ordervalue = float(input("\nEnter order value: "))
print("\nDo you want to pay £5.00 for next day delivery?")
postcode = int(input("Enter 1 for 2nd class delivery, 2 for next day delivery: "))
# Calculations
postcost = 0
if ordervalue <= 0:
    print("\nInvalid value")
    ordervalue = 0
elif ordervalue >= 15 and postcode == 1:
    postcost = 0
elif ordervalue <=15 and postcode == 1:
    postcost = 3.5
else:
    postcost = 5
cost = ordervalue + postcost
print("\nThe postage charge is £"+str(postcost))
print("\nThe total charge is £"+str(cost))
# Exit
input("\nPress ENTER to exit")
