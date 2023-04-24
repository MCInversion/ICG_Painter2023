# ===============================================================================================
# This is the main application class for the ICGPainter Tkinter application.
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

import src.util as Util
from src.paint_brush import PaintBrush
from src.defaults import *
from src.image_project import *
from Symmetry import Symmetry

global brush_icon_img

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.geometry("{}x{}".format(default_img_width, default_img_height))

        self.toolbar_frame = tk.Frame(self.parent)
        self.toolbar_frame.pack(side="top", fill="x")

        brush_icon_img = PhotoImage(file=r"res\Brush.png")
        self.brush_button = Button(self.toolbar_frame, image=brush_icon_img)
        self.brush_button.image = brush_icon_img
        self.brush_button.pack(side="left")

        eraser_icon_img = PhotoImage(file=r"res\kresli_h.png")
        self.hsymmetry_button = Button(self.toolbar_frame, image=eraser_icon_img, command=self.v)
        self.hsymmetry_button.image = eraser_icon_img
        self.hsymmetry_button.pack(side="left")

        eraser_icon_img = PhotoImage(file=r"res\kresli_v.png")
        self.vsymmetry_button = Button(self.toolbar_frame, image=eraser_icon_img, command=self.h)
        self.vsymmetry_button.image = eraser_icon_img
        self.vsymmetry_button.pack(side="left")

        eraser_icon_img = PhotoImage(file=r"res\kresli.png")
        self.symmetry_button = Button(self.toolbar_frame, image=eraser_icon_img, command=self.a)
        self.symmetry_button.image = eraser_icon_img
        self.symmetry_button.pack(side="left")

        self.canvas = Canvas(self.parent, bg = default_img_color, height = default_img_height, width = default_img_width)
        self.canvas.place(x=0, y=default_toolbar_height)

        self.image_project = ImageProject(self.canvas)
        self.image_project.new()

        self.brush = PaintBrush(self.canvas, default_brush_color, default_brush_width)
        self.brush_button.bind('<ButtonPress-1>', self.brush.change_width)

        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="New", command=self.image_project.new)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        self.canvas.bind('<ButtonPress-1>', self.brush.draw_pixel) # bind left button to self.brush.draw_pixel
        self.canvas.bind('<B1-Motion>', self.brush.draw_pixel) # bind mouse move to self.brush.draw_pixel         
        self.parent.bind('<ButtonPress-2>', self.brush.change_color) # bind scroll wheel click to colorpicker

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("PNG Image files", "*.png;")])
        if file_path:
            self.image_project.open(file_path)

    def save_file(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_project.save(file_path)

    def change_brush_color(self, event):
        if event.num == 3:
            if self.brush.tool in ["a", "v", "h"]:
                if self.brush.tool == "a":
                    self.color_picker(self.a, 'normal')
                elif self.brush.tool == "v":
                    self.color_picker(self.v, 'vertical')
                elif self.brush.tool == "h":
                    self.color_picker(self.h, 'horizontal')

    def color_picker(self, command, *args):
        color = colorchooser.askcolor(title="Choose color")
        if color:
            self.brush.change_color(color[1])
            command(*args)

    def a(self):
        self.canvas.bind('<ButtonPress-1>', lambda event: self.draw(event, 'normal'))
        self.canvas.bind('<B1-Motion>', lambda event: self.draw(event, 'normal'))

    def v(self):
        self.canvas.bind('<ButtonPress-1>', lambda event: self.draw(event, 'vertical'))
        self.canvas.bind('<B1-Motion>', lambda event: self.draw(event, 'vertical'))

    def h(self):
        self.canvas.bind('<ButtonPress-1>', lambda event: self.draw(event, 'horizontal'))
        self.canvas.bind('<B1-Motion>', lambda event: self.draw(event, 'horizontal'))

    def draw(self, event, sym_type):
        s = Symmetry(event.x, event.y, 10, self.canvas, self.brush.color)
        s.kresli(sym_type)

    def klik(self,event,typ):
        s = Symmetry(event.x, event.y,10,self.canvas)
        s.kresli(typ)

if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("res/ICGIcon.ico")
    root.title("Painter")

    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()
