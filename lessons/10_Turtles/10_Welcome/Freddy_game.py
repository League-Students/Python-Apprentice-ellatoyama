import turtle

tina = turtle.Turtle
screen = turtle.Screen()
Screen.setup(600,600)

cam_colors = ['red','black','white','blue','green']

def open_cam_1():
    print("cam 1 open")
    screen.bgcolor(cam_colors[0])
def open_cam_2():
    print("cam 2 open")
    screen.bgcolor(cam_colors[0])




screen.listen()
screen.onekey(open_cam_1, "1")

turtle.exitonclick()
