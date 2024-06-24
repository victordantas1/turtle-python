import random
from turtle import Turtle

tur = Turtle()
steps_width = 200
steps_heigth = 20
degree = 90
color = ['red', 'blue', 'grey']

n_tri = int(input())

for i in range(n_tri):
    color_i = random.randint(0, 2)
    tur.begin_fill()
    tur.color('black', color[color_i])
    tur.forward(steps_width)
    tur.right(degree)
    tur.forward(steps_heigth)
    tur.right(degree)
    tur.forward(steps_width)
    tur.right(degree)
    tur.forward(steps_heigth)
    tur.end_fill()
    tur.penup()
    tur.forward(40)
    tur.right(90)
    tur.pendown()

tur.screen.mainloop()
