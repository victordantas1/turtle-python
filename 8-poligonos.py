import tkinter as tk
from math import *

def imprime_linhas_centrais(canvas, centro_x, centro_y, size): 
    canvas.create_line(centro_x, centro_y, centro_x + size, centro_y, activewidth=10)
    canvas.create_line(centro_x, centro_y, centro_x, centro_y + size, activewidth=10)
    canvas.create_line(centro_x, centro_y, centro_x - size, centro_y, activewidth=10)
    canvas.create_line(centro_x, centro_y, centro_x, centro_y - size, activewidth=10)

def imprime_triangulo(canvas, centro_x, centro_y, size):
    lado = 0.9 * size
    esp = size * 0.1
    altura = sqrt(pow(lado, 2) - pow(lado // 2, 2))
    canvas.create_polygon([centro_x + esp, centro_y - esp, centro_x + esp + lado, centro_y - esp, (2 * centro_x + 2 * esp + lado) // 2, centro_y - altura - esp], outline='black', fill='blue')

def imprime_quadrado(canvas, centro_x, centro_y, size):
    lado = 0.9 * size
    esp = size * 0.1
    canvas.create_polygon([centro_x + esp, centro_y + esp, centro_x + esp + lado, centro_y + esp, centro_x + esp + lado, centro_y + esp + lado, centro_x + esp, centro_y + esp + lado], outline="black", fill='red')

def imprime_circulo(canvas, centro_x, centro_y, size):
    raio = 0.45 * size
    esp = size * 0.1
    canvas.create_oval(centro_x - size, centro_y + esp, centro_x - size + 2 * raio, centro_y + esp + 2 * raio, outline='black', fill='green', width=1)

window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)

centro_x = 800 / 2
centro_y = 600 / 2
size = int(input())

imprime_linhas_centrais(canvas, centro_x, centro_y, size)
imprime_triangulo(canvas, centro_x, centro_y, size)
imprime_quadrado(canvas, centro_x, centro_y, size)
imprime_circulo(canvas, centro_x, centro_y, size)

canvas.pack()
window.mainloop()