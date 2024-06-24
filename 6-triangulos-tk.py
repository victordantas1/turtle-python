import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)
canvas.create_polygon([10, 20, 160, 20, 85, 140], outline="black", fill="red")
canvas.create_polygon([190, 20, 115, 140, 265, 140], outline="black", fill="yellowgreen")
canvas.create_polygon([220, 20, 370, 20, 295, 140], outline="black", fill="blue")
canvas.pack()

window.mainloop()