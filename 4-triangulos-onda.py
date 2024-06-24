from turtle import Turtle

tur = Turtle()
WIDTH_SCREEN = 600
HEIGTH_SCREEN = 400

tur.screen.screensize(WIDTH_SCREEN, HEIGTH_SCREEN)

tur.penup()
tur.setpos((WIDTH_SCREEN // 2, 0))   
tur.pendown()

num_tri = int(input())

tur.left(180)
segment_width = WIDTH_SCREEN / num_tri + 1
tri_side = 80
tur.pensize(3)
tur.forward(segment_width - (tri_side / 2))
for i in range(num_tri):
    tur.right(60)
    tur.forward(tri_side)
    tur.left(120)
    tur.forward(tri_side)
    tur.right(60)
    if i < num_tri - 1:
        tur.forward(segment_width - tri_side)
    
tur.forward(segment_width - (tri_side / 2))
tur.screen.mainloop()

