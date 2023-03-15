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

global brush_icon_img

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.geometry("{}x{}".format(default_img_width, default_img_height))

        self.toolbar_frame = tk.Frame(self.parent)
        self.toolbar_frame.pack(side=TOP, fill="x")

        brush_icon_img = PhotoImage(file=r"res\Brush.png")
        self.brush_button = Button(self.toolbar_frame, image=brush_icon_img)
        self.brush_button.image = brush_icon_img
        self.brush_button.pack(side=LEFT)

        self.canvas = Canvas(self.parent, bg = default_img_color, height = default_img_height, width = default_img_width)
        self.canvas.place(x=0, y=default_toolbar_height)
        self.canvas.pack()

        self.image_project = ImageProject(self.canvas)
        self.image_project.new()

        self.brush = PaintBrush(self.image_project, default_brush_color, default_brush_width)
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

        self.parent.bind('<ButtonPress-1>', self.brush.draw_pixel) # bind left button to self.brush.draw_pixel
        self.parent.bind('<B1-Motion>', self.brush.draw_pixel) # bind mouse move to self.brush.draw_pixel         
        self.parent.bind('<ButtonPress-2>', self.brush.change_color) # bind scroll wheel click to colorpicker

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("PNG Image files", "*.png;")])
        if file_path:
            self.image_project.open(file_path)

    def save_file(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_project.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("res/ICGIcon.ico")
    root.title("Painter")

    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()