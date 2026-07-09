import turtle
tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
tina.speed(0)
tina.shape('turtle')
def fractal_stuff(size,depth):
    if depth == 0:
        for i in range(10):
            tina.forward(size)
            tina.left(36)
    else:
        for in




turtle.exitonclick()