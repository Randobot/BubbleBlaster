from tkinter import *
window = Tk()
window.title('Alien')
c = Canvas(window, width=400, height=300)
c.pack()
main= c.create_oval(100,150,300,250,outline='lime',fill='lime')
eyes = c.create_oval(170,70,230,130,outline='white',fill='white')
pupil = c.create_oval( 190,90,210,110, outline='black',fill='black')
Neck =  c.create_oval(200, 150, 200 ,130, fill='black')
Mouth = c.create_oval(150,200,250,240, outline='red',fill='red')
hat = c.create_polygon(180,75,220,75,200,20, outline='blue', fill='blue')

def open():
    c.itemconfig(Mouth, outline='black', fill='black')

def close():
    c.itemconfig(Mouth, fill='red')

def blink():
    c.itemconfig(eyes, outline='lime', fill='lime')
    c.itemconfig(pupil, state=HIDDEN)

def nblink():
    c.itemconfig(eyes, fill='white')
    c.itemconfig(pupil, state=NORMAL)

    
