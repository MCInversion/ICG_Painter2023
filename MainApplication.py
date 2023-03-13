from tkinter import *
import tkinter as tk
from src.PaintBrush import PaintBrush

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.canvas = Canvas(self, bg = "blue", height = 400, width = 500)
        self.canvas.pack()
        self.brush = PaintBrush(self.canvas, "red", 50)
        root.bind('<ButtonPress-1>', self.brush.draw_pixel) # bind left button to self.brush.draw_pixel
        root.bind('<B1-Motion>', self.brush.draw_pixel) # bind mouse move to self.brush.draw_pixel         
        root.bind('<ButtonPress-2>', self.brush.change_color) # bind scroll wheel click to colorpicker

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()