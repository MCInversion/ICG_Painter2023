# ===============================================================================================
# This is the main application class for the ICGPainter Tkinter application.
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

import src.util as Util
from src.paint_brush import PaintBrush
from src.ruler_and_angle import Ruler, Angle

from src.defaults import *
from src.image_project import *

global brush_icon_img, ruler_icon_img, angle_icon_img

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

        ruler_icon_img = PhotoImage(file=r"res\Ruler.png")
        self.ruler_button = Button(self.toolbar_frame, image=ruler_icon_img)
        self.ruler_button.image = ruler_icon_img
        self.ruler_button.pack(side="left")

        angle_icon_img = PhotoImage(file=r"res\Angle.png")
        self.angle_button = Button(self.toolbar_frame, image=angle_icon_img)
        self.angle_button.image = angle_icon_img
        self.angle_button.pack(side="left")

        self.reporting_label = Label(self.toolbar_frame,text="REPORTING LABEL",justify=RIGHT)
        self.reporting_label.pack(side="right")

        self.canvas = Canvas(self.parent, bg = default_img_color, height = default_img_height, width = default_img_width)
        self.canvas.place(x=0, y=default_toolbar_height)

        self.image_project = ImageProject(self.canvas)
        self.image_project.new()

        self.brush = PaintBrush(self.canvas, default_brush_color, default_brush_width)
        self.brush_button.bind('<ButtonPress-1>', self.set_active_tool_brush)

        self.ruler = Ruler(self.canvas, self.reporting_label)
        self.ruler_button.bind('<ButtonPress-1>', self.set_active_tool_ruler)

        self.angle = Angle(self.canvas, self.reporting_label)
        self.angle_button.bind('<ButtonPress-1>', self.set_active_tool_angle)

        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="New", command=self.image_project.new)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        self.set_active_tool_brush(None)

    def do_nothing(self, p):
        pass

    def set_active_tool_brush(self, p):
        self.canvas.bind('<ButtonPress-1>', self.brush.draw_pixel)
        self.canvas.bind('<B1-Motion>', self.brush.draw_pixel)       
        self.parent.bind('<ButtonPress-2>', self.brush.change_color)
        self.reporting_label.config(text='')

    def set_active_tool_ruler(self, p):
        self.canvas.bind('<ButtonPress-1>', self.ruler.process_click)
        self.canvas.bind('<B1-Motion>', self.do_nothing)
        self.parent.bind('<ButtonPress-2>', self.do_nothing)
        self.ruler.clear(None)

    def set_active_tool_angle(self, p):
        self.canvas.bind('<ButtonPress-1>', self.angle.process_click)
        self.canvas.bind('<B1-Motion>', self.do_nothing)       
        self.parent.bind('<ButtonPress-2>', self.do_nothing)
        self.angle.clear(None)
    
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
label= Label(frame1,text="Label",justify=LEFT)
label.pack(side=LEFT)



