# Question 2 Phone Bill program
# Programmer: Leon Chung -- Date: October 10, 2016

# The Problem:
"""
Complete the pseudo code program.
# Program to output maximum month’s phone bill
MonthName [“January”, “February”, “March”, “April”, “May”, “June”, “July”, “August”,
            “September”, “October”, “November”, “December”]
# Define an array to hold the phone bills for each month
"""

# Pseudo code
"""
MonthName = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
PhoneBill = [0,0,0,0,0,0,0,0,0,0,0,0]
MaxBill = 0
FOR number IN range (0,12) THEN
    OUTPUT ("Input temperature for {0}: ".format(MonthName[number])
    PhoneBill[number]= USERINPUT
    IF PhoneBill[number] > MaxBill THEN
        MaxBill = PhoneBill[number]
        MaxMonth = MonthName[number]
OUTPUT ("The maximum phone bill is: {0}, {1}".format(MaxMonth,MaxBill))
"""

# Program
# Welcome text
print("Welcome to Phone Bill program")

# Calculations
MonthName = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
PhoneBill = [0,0,0,0,0,0,0,0,0,0,0,0]
MaxBill = 0
for number in range (0,12):
    PhoneBill[number]=float(input("Input temperature for {0}: ".format(MonthName[number])))
    if PhoneBill[number] > MaxBill:
        MaxBill = PhoneBill[number]
        MaxMonth = MonthName[number]
print("\nThe maximum phone bill is: {0}, {1}".format(MaxMonth,MaxBill))

# Exit
input("Press ENTER to exit")

