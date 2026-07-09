tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')

def fractal_square_stuff(size,depth,color):
    tina.penup()
    if depth == 0: 
        tina.begin
