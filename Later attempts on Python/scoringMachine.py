# Program for grading and calculating scores
# Programmer: Leon    Date: 1,November

# The Problem
"""
A teacher needs a program to record marks for
a class of 30 students who have sat three computer science tests.
"""

# Pseudo code
"""
listOfStudent = []
scores = []
test1 = []
test2 = []
test3 = []
FOR n IN (0,30)
    OUTPUT("Enter the names of student: ")
    listOfStudent = USERINPUT
    OUTPUT("Enter score of test 1: ")
    test1 = USERINPUT
    WHILE test1 < 0 OR test1 > 20
        OUTPUT("Enter again: ")
        test1 = USERINPUT
    OUTPUT("Enter score of test 2: ")
    test2 = USERINPUT
        WHILE test2 < 0 OR test2 > 25
        OUTPUT("Enter again: ")
        test2 = USERINPUT
    OUTPUT("Enter score of test 3: ")
    test3 = USERINPUT
        WHILE test3 < 0 OR test3 > 30
        OUTPUT("Enter again: ")
        test3 = USERINPUT
    total = test1 + test2 + test3
    scores = total
    OUTPUT(listOfStudent[number],scores[number])
    totalForAverage = totalForAverage + score[number]
ENDFOR
average = totalForAverage/30
OUTPUT(average)
FOR number IN range(0,30):
    if scores[number] > highScore:
        highScore = scores[number]
        name = listOfStudent[number]
OUTPUT("The student with highest score is "+ name +" with a score of "+highScore)
"""

# Program
# Task 1
listOfStudent = []
scores = []
test1 = []
test2 = []
test3 = []
total = 0
print("!!! Welcome to the Scoring Machine program !!!")
for number in range(0,3):
    listOfStudent.append(input("\nEnter the names of student: "))
    test1.append(int(input("Enter score of test 1 out of 20: ")))
    while test1[number] < 0 or test1[number] > 20:
        test1[number] = int(input("Enter again: "))
    test2.append(int(input("Enter score of test 2 out of 25: ")))
    while test2[number] < 0 or test2[number] > 25:
        test2[number]= int(input("Enter again: "))
    test3.append(int(input("Enter score of test 3 out of 30: ")))
    while test3[number] < 0 or test3[number] > 30:
        test3[number] = int(input("Enter again: "))
    scores.append(test1[number] + test2[number] + test3[number])
    print(listOfStudent[number].title()+ " scored a total of " +str(scores[number]))
# Task 2
for number in range(0,3):
    total += scores[number]
average = round(total/len(listOfStudent),3)
print("\nThe total score of the whole class is "+str(total))
print("The average score of the whole class is "+str(average))
# Task 3
highScore = 0
for number in range(0,3):
    if scores[number] > highScore:
        highScore = scores[number]
        name = str(listOfStudent[number].title())
print("The student with highest score is "+ name +" with a score of "+str(highScore))
input("Press ENTER to exit")