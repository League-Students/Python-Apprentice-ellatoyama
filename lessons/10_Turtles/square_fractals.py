tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')

def nudge(color):
    color+= 1 + random.random() * 0.1

def fractal_square_stuff(size,depth,color):
    tina.penup()
    if depth == 0: 
        tina.begin_fill()
        tina.color(color)
        for i in range(4):
            tina.forward(size)
            tina.left(90)
        tina.end_fill()
    else:
