# Question 4 Floor Turtle program
# Programmer: Leon Chung -- Date: September 20, 2016

# The Problem:

# Import the turtle module
import turtle

# Activate window for drawing
window = turtle.Screen()
window.bgcolor("black")

# Activate pen
pen = turtle.Pen()
pen.color("yellow")
pen.pensize(5)
pen.speed(5)

# Complete the set of instructions to draw the shape shown below in bold lines, starting at the point marked X.
# Move pen to position
# 1
pen.up()
pen.goto(50,50)
pen.down()
pen.left(90)
for X in range(0,4):
        pen.forward(100)
        pen.right(90)
# 2
distance = 0
for X in range(0,3):
    pen.up()
    pen.goto(distance,-60)
    pen.down()
    for x in range(0,4):
        pen.forward(50)
        pen.right(90)
    distance += 100
# 3
distance = 0
pen.up()
pen.goto(-200,50)
pen.down()
pen.left(180)
for X in range(0,8):
    for X in range(0,2):
        pen.forward(distance)
        pen.right(90)
    distance += 50
window.mainloop()

