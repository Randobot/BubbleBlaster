from tkinter import *

window =Tk()
window.title('CharacterM')

c = Canvas(window, height=600, width=600, bg='black')
c.pack()

ball = c.create_oval(50,50,100,100,fill='white')

def move(event):
    key = event.keysym
    if key == "Up":
        c.move(ball,0,-10)
    elif key == "Down":
        c.move(ball,0,10)
    elif key == "Left":
        c.move(ball,-10,0)
    elif key == "Right":
        c.move(ball,10,0)

c.bind_all('<Key>',move)
