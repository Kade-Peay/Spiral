import turtle
import time

t = turtle.Turtle()
wn = turtle.Screen()

def draw():
    colors = ['blue', 'purple', 'red', 'yellow', 'orange', 'green',]

    t.pensize(5)
    wn.bgcolor('black')
    t.speed(1000)

    for x in range(700):
        t.pencolor(colors[x % len(colors)])
        t.pensize(x / 50)
        t.forward(x)
        t.left(59)


draw()
time.sleep(5)