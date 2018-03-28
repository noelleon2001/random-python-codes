# Question 2 Floor Turtle program
# Programmer: Leon Chung -- Date: September 23, 2016

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
pen.up()
pen.goto(0,0)
pen.down()
pen.left(90)
for x in range(0,2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)

pen.up()
pen.goto(200,-50)
pen.down()
pen.left(180)
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.left(90)

window.mainloop()