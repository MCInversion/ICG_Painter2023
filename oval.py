from tkinter import *
import tkinter as tk

import src.util as Util
from src.paint_brush import PaintBrush
from src.defaults import *
from src.image_project import *

class oval(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.parent.geometry("{}x{}".format(default_img_width, default_img_height))
        
        self.pos = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        
        self.canvas = Canvas(self.parent, bg = default_img_color, height = default_img_height, width = default_img_width)
        self.canvas.place(x=0, y=default_toolbar_height)        
        self.ov = self.canvas.create_oval(0, 0, 0, 0)
        
        self.canvas.bind('<ButtonRelease-1>', self.klik)
        self.canvas.bind('<Motion>', self.process)
        self.canvas.master.bind('<Escape>', self.cancel)

    def klik(self, event):
        if self.pos == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.pos = 1
        elif self.pos == 1:
            self.x2 = event.x
            self.y2 = event.y
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)
            self.pos = 0
    
    def process(self, event):
        if self.pos == 1:
            self.x2 = event.x
            self.y2 = event.y
            self.canvas.delete(self.ov)
            self.ov = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)

    def cancel(self, event):
        if self.pos == 1:
            self.canvas.delete(self.ov)
            self.pos = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.title('oval')
            
    oval(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()
