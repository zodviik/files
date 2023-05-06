import tkinter, random, time
class Ball():
    def __init__(self, canvas:tkinter.Canvas, color, paddle):
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,15,15,fill=color)
        canvas.move(self.id, 240, 150)
        self.x = random.randint(-3,2)+0.5
        self.y = -3
        self.paddle = paddle
        self.run = True
        self.score = 0
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 500:
            self.run = False
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
        if self.hit(pos):
            self.y = -3
            self.score += 1
    def hit(self,pos):
        pos_p = self.canvas.coords(self.paddle.id)
        if pos[2] > pos_p[0] and pos[0] < pos_p[2]:
            if pos[3] > pos_p[1] and pos[3] < pos_p[3]:
                return True
        return False
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
ball = Ball(canvas, "red", padlle)
score_text = canvas.create_text(430,20,text=f"Счёт: {ball.score}",font=("Arial",20))

while ball.run:
    canvas.itemconfig(score_text, text=f"Счет: {ball.score}")
    ball.draw()
    padlle.draw()
    okno.update()
    okno.update_idletasks()
    time.sleep(0.01)
canvas.create_text(250,250,text="Вы проиграли(")
okno.update()
time.sleep(3)