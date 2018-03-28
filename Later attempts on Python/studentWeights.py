# Program for calculating student's weights
# Programmer: Leon    Date: 7,November

# The Problem
"""
Keeping record of weights of each pupil.
"""

# Pseudo code
"""
studentNames = []
weight1 = []
weight2 = []
difference = []

FOR number IN (0,30)
    OUTPUT "Enter the name of student: "
    studentNames = USERINPUT
    OUTPUT "Enter the weight of student: "
    weight1 = USERINPUT
    WHILE weight1[number] < 30 OR weight1[number] > 100
        OUTPUT "Invalid data, enter again: "
        weight1 = USERINPUT
    ENDWHILE

    OUTPUT (studentNames[number], weight1[number])
    OUTPUT "Enter the weight of student at the last day of term: "
    weight2 = USERINPUT
    WHILE weight2[number] < 30 OR weight2[number] > 100
        OUTPUT "Invalid data, enter again: "
        weight2 = USERINPUT
    ENDWHILE

    OUTPUT (studentNames[number], weight2[number])
    difference = weight2 - weight1
    IF difference[number] > 2.5 THEN
        OUTPUT (studentNames[number],difference[number])
        OUTPUT ("It is a rise")
    ENDIF
    IF difference[number] < -2.5 THEN
        difference[number] = difference[number] + (2 * difference[number])
        OUTPUT (studentNames[number],difference[number])
        OUTPUT ("It is a fall")
    ENDIF
"""

# Program
studentNames = []
weight1 = []
weight2 = []
difference = []
print("!!!!Welcome to the Student Weight program!!!!")

for number in range(0,2):
    studentNames.append(input("\nEnter the name of student: "))

    weight1.append(float(input("\nEnter the weight of student on the first day of term: ")))
    while weight1[number] < 25 or weight1[number] > 100:
        weight1[number]= float(input("Invalid data, enter again: "))

    weight2.append(float(input("Enter the weight of student at the last day of term: ")))
    while weight2[number] < 25 or weight2[number] > 100:
        weight2[number]= float(input("Invalid data, enter again: "))
    difference.append(weight2[number] - weight1[number])
print()
for number in range(0,2):
    print()
    if difference[number] > 2.5 :
        print(studentNames[number]+" has a difference of weight of "+str(difference[number]))
        print("It is a rise, your child is getting fat")
    elif difference[number] < -2.5:
        difference[number] = -difference[number]
        print(studentNames[number]+" has a difference of weight of "+str(difference[number]))
        print("It is a fall, you need to feed your child")
