"""
# 20_Crazy_Spiral.py

Make your own crazy spiral with a pattern like
in 10_Flaming_Ninja_Star.py, but use what you've learned about loops

uid: zfzMbyH7
name: Crazy Spiral
"""

import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def get_next_color(i):
    return colors[i % len(colors)]

turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()

base_size = 200  # the size of the black part of the star
flame_size = 130  # the length of the flaming arms

tina = turtle.Turtle()
tina.shape("turtle")
tina.width(2)
tina.speed(0)

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(tina):
    """Make a shape with turtle t. Make it go left or right or
# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make,
# for example 100, or a list of numbers.

num_shapes = ...

for i in range(500):
    tina.pencolor(get_random_color())
    tina.fillcolor(get_random_color())
    tina.begin_fill()
    tina.forward(30)
    tina.left(60)
    tina.forward(15)
    tina.right(35)
    tina.forward(70)
    tina.right(70)
    tina.forward(60)
    tina.right(135)
    tina.forward(120)
    tina.endfill()

    
turtle.done