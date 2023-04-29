from tkinter import*
import time
def right(e):
    canvas.move(a,2,0)
okno = Tk()
canvas = Canvas(okno, width=500, height=500)
canvas.pack()
canvas.create_line(0,100,50,150)
a = canvas.create_rectangle(100,50,200,150,width=5,activefill="purple")
canvas.create_oval(100,50,200,150,fill="red",outline="blue",width=3)
canvas.create_polygon(100,50,
                      150,70,
                      125,85)
canvas.bind_all("<Right>", right)
okno.mainloop()