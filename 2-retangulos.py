from turtle import Turtle

tur = Turtle()
steps_width = 200
steps_heigth = 20
degree = 90
color = ['red', 'blue']

for i in range(2):
    tur.begin_fill()
    tur.color('black', color[i])
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
