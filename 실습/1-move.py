from tkinter import *
tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

my_t = canvas.create_polygon(10,10,10,60,50,35,fill='pink', outline='black')

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(my_t, 0, -3)
        canvas.itemconfig(my_t, fill='pink')
    elif event.keysym == 'Down':
        canvas.move(my_t, 0, 3)
        canvas.itemconfig(my_t, fill='grey')
    elif event.keysym == 'Left':
        canvas.move(my_t, -3, 0)
        canvas.itemconfig(my_t, fill='lightblue')
    else :
        canvas.move(my_t, 3, 0)
        canvas.itemconfig(my_t, fill='white')

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
