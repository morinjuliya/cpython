import turtle

from itertools import cycle
color = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size):
    turtle.pencolor(next(color))
    turtle.circle(size)
    draw_circle(size+5)
    


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)
