import tkinter as tk

def cria_circulo(x1, y1, raio, cor):
    canvas.create_oval(x1, y1, x1 + raio, y1 + raio, outline=cor, width=10)

window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)
cria_circulo(10, 20, 200, '#0885c2')
cria_circulo(105, 120, 200, '#fbb132')
cria_circulo(230, 20, 200, 'black')
cria_circulo(325, 120, 200, '#1c8b3c')
cria_circulo(450, 20, 200, '#ed334e')
canvas.pack()
window.mainloop()