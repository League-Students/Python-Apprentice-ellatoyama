import turtle

tina = turtle.Turtle
screen = turtle.Screen()
Screen.setup(600,600)

cam_colors = ['red','black','white','blue','green']

screen.listen()
screen.onekey(open_cam_1, '1')

turtle.exitonclick()
