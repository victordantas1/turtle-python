from turtle import *

degree = 120
step = 200

tur = Turtle()
tur.begin_fill()
tur.color('black', 'red')
tur.left(degree)
tur.forward(step)
tur.left(degree)
tur.forward(step)
tur.left(degree)
tur.forward(step)
tur.end_fill()

tur.screen.mainloop()
