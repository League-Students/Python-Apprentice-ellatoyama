import turtle


tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')
def fractal_stuff(size,depth):
    if depth == 0:
        for i in range(10):
            tina.forward(size)
            tina.left(36)
    else:
        for i in range(10):
            fractal_stuff(size/2,depth-1)
            tina.forward(size)
            tina.left(36)
tina.penup()
tina.goto(-225,-225)
tina.pendown()

fractal_stuff(200,4)

turtle.exitonclick()