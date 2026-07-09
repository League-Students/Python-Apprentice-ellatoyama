tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')

def nudge(color):
    color+= 1 + random.random() * 0.1 - 0.05
    return color % 1

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
        for i in range(4):
            color = (nudge(color[0]),nudge(color[1]),nudge(color[2]))
            fractal_squar_stuff(size/2,depth-1,color)
            tina.forward(sizew)
