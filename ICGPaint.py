# ===============================================================================================
# This is the main application class for the ICGPainter Tkinter application.
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

from src.paint_brush import PaintBrush
from src.defaults import *
from src.image_project import *
from src.bindings import *
from src.command import *

global brush_icon_img

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.geometry("{}x{}".format(default_img_width, default_img_height))

        self.toolbar_frame = tk.Frame(self.parent)
        self.toolbar_frame.pack(side="top", fill="x")

        brush_icon_img = PhotoImage(file=r"res\Brush.png")
        self.brush_button = add_tool_button(self.toolbar_frame, brush_icon_img, command = DrawPixelCommand(self.brush.draw_pixel), accelerator="Ctrl+B")

        self.canvas = Canvas(self.parent, bg = default_img_color, height = default_img_height, width = default_img_width)
        self.canvas.place(x = 0, y = default_toolbar_height)

        self.image_project = ImageProject(self.canvas)
        self.image_project.new()

        self.brush = PaintBrush(self.canvas, default_brush_color, default_brush_width)
        self.brush_button.bind('<ButtonPress-1>', self.brush.change_width)

        self.command_menu = CommandMenu(self.parent)
        self.command_menu.add_command_with_binding("New", NewImageCommand(self.image_project), "Ctrl+N")
        self.command_menu.add_command_with_binding("Open", OpenFileCommand(self.image_project), "Ctrl+O")
        self.command_menu.add_command_with_binding("Save", SaveFileCommand(self.image_project), "Ctrl+S")
        self.command_menu.add_command_with_binding("Exit", QuitCommand(self), "Ctrl+Q")
        self.command_menu.add_separator()
        
        self.parent.config(menu=self.command_menu.menu)
        self.canvas.bind('<ButtonPress-1>', self.brush.draw_pixel)
        self.canvas.bind('<B1-Motion>', self.brush.draw_pixel)
        self.parent.bind('<ButtonPress-2>', self.brush.change_color)

if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("res/ICGIcon.ico")
    root.title("Painter")

    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()