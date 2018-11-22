from random import *
from tkinter import *
size = 600
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    color = choice(['orchid','green','orange','yellow','lime'])
    x0 = randint(0,size)
    y0 = randint(0,size)
    d = randint(0,size/5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=color)
    window.update()
