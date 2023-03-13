# ===============================================================================================
# This is the main application class for the ICGPainter Tkinter application.
# ===============================================================================================

from tkinter import *
import tkinter as tk
import src.Util as Util
from src.PaintBrush import PaintBrush

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="New", command=Util.do_nothing)
        self.filemenu.add_command(label="Open", command=Util.do_nothing)
        self.filemenu.add_command(label="Save", command=Util.do_nothing)
        self.filemenu.add_command(label="Save as...", command=Util.do_nothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        root.config(menu=self.menubar)

        self.canvas = Canvas(self, bg = "white", height = 400, width = 500)
        self.canvas.pack()
        self.brush = PaintBrush(self.canvas, "red", 50)

        root.bind('<ButtonPress-1>', self.brush.draw_pixel) # bind left button to self.brush.draw_pixel
        root.bind('<B1-Motion>', self.brush.draw_pixel) # bind mouse move to self.brush.draw_pixel         
        root.bind('<ButtonPress-2>', self.brush.change_color) # bind scroll wheel click to colorpicker

if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("res/ICGIcon.ico")
    root.title("Painter")

    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()