import tkinter, random, time
class Ball():
    def __init__(self, canvas:tkinter.Canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,15,15,fill=color)
        canvas.move(self.id, 240, 150)
        self.x = random.randint(-3,2)+0.5
        self.y = -3
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 500:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
class Padlle():
    def __init__(self, canvas:tkinter.Canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        canvas.move(self.id, 200, 440)
        self.x = 0
        self.canvas.bind_all("<Left>",self.left)
        self.canvas.bind_all("<Right>",self.right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= 500:
            self.x = -2
    def left(self,e):
        self.x = -2
    def right(self,e):
        self.x = 2
        
okno = tkinter.Tk()
okno.resizable(0,0)
okno.title("ПингПонг")
okno.wm_attributes("-topmost",1)
canvas = tkinter.Canvas(okno, height=500, width=500, bd=0, highlightthickness=0)
canvas.pack()
okno.update()
padlle = Padlle(canvas, "black")
ball = Ball(canvas, "red")
while True:
    ball.draw()
    padlle.draw()
    okno.update()
    okno.update_idletasks()
    time.sleep(0.01)