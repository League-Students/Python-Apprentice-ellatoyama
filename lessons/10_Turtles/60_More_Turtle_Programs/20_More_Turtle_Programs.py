"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Change the Turtle's Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern.
"""

# Double-click to copy!

import turtle                               # Import the turtle module

screen = turtle.Screen()                # Set up the screen
screen.setup(width=600, height=600)     # Set the size of the window
screen.bgcolor('white')                 # Set the background color

t1 = turtle.Turtle()                    # Create the first turtle
t1.penup()                              # Lift the pen to move without drawing
t1.shape("turtle")                      # Set the shape of the turtle

t2 = turtle.Turtle()                    # Create the second turtle
t2.penup()                              # Lift the pen to move without drawing
t2.shape("arrow")                       # Set the shape of the turtle

# Move both turtles in a loop
for i in range(-200, 200):
    t1.goto(i, i)
    t2.goto(i, -i)
```