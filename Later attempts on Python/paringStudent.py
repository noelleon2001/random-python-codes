# Program for grading and calculating scores
# Programmer: Leon    Date: 10,November

# The Problem
"""
An app for paring students randomly
"""

# Pseudo code
"""
listOfStudent = []
even = FALSE
FOR number IN (0,30)
    OUTPUT("Enter the names of student: ")
    listOfStudent = USERINPUT
    IF (mod(listOfStudent[number],2) = 0) THEN
        even = TRUE
IF even = TRUE THEN
    n = len(listOfStudent)/2
    FOR number IN (0,n)
        student1 = random(listOfStudent)
        DELETE listOfStudent[number]
        student2 = random(listOfStudent)
        DELETE listOfStudent[number]
        print(student1,student2)
ELSE
    listOfStudent = INPUT "Imaginary Friend"
    n = len(listOfStudent)/2
    FOR number IN (0,n)
        student1 = random(listOfStudent)
        DELETE listOfStudent[number]
        student2 = random(listOfStudent)
        DELETE listOfStudent[number]
        print(student1,student2)
"""

# Program
import random
listOfStudent = []
h = 0
while h != "":
    h = input("\nEnter the names of student: ")
    listOfStudent.append(h)
if len(listOfStudent)%2 :
    for number in range(0,(len(listOfStudent)/2)):
        student1 = random.choice(listOfStudent)
        del listOfStudent[number]
        student2 = random.choice(listOfStudent)
        del listOfStudent[number]
        print(student1,student2)
else:
    listOfStudent.append("Imaginary Friend")
    n = len(listOfStudent)/2
    for number in range(0,n):
        student1 = random.choice(listOfStudent)
        del listOfStudent[number]
        student2 = random.choice(listOfStudent)
        del listOfStudent[number]
        print(student1,student2)
