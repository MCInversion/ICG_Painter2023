from tkinter import Toplevel, Label, Entry, Button

class eraser:
    def __init__(self, master, canvas):
        self.master = master
        self.canvas = canvas
        self.a = None
        self.canvas.bind('<B1-Motion>', self.klik)
        self.canvas.bind('<ButtonPress-1>', self.klik)

    def popup(self):
        if self.master is not None:
            self.top = Toplevel(self.master)
            self.l = Label(self.top, text="Size of eraser:")
            self.l.pack()
            self.e = Entry(self.top)
            self.e.pack()
            self.e.focus_set()
            self.e.bind("<Return>", lambda event: self.cleanup())
            self.b = Button(self.top, text='Ok', command=self.cleanup)
            self.b.pack()

    def cleanup(self):
        if self.master is not None:
            value = self.e.get()
            self.change_a(value)
            self.top.destroy()

    def change_a(self, value):
        if value == '':
            self.a = 10
        else:
            if value.isdigit():
                value = int(value)
                self.a = value if value > 0 else None
            else:
                self.a = None

    def klik(self, event):
        if self.a is not None:
            fill_color = self.canvas.cget('background')
            x1 = event.x - self.a
            y1 = event.y - self.a
            x2 = event.x + self.a
            y2 = event.y + self.a
            self.canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline='')


