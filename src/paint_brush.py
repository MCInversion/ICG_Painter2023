# ===============================================================================================
# A paint brush object with adjustable width and color
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintBrush():
    def __init__(self, canvas, color, width):
        self.color = color
        self.width = width
        self.canvas = canvas
 
    def draw_pixel(self, p):
        x, y = p.x, p.y
        r = int(self.width / 2)
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color, outline="")

    def change_color(self, p):
        colors = askcolor(title="Tkinter Color Chooser")
        self.color = colors[1]
        
    def change_width(self, p):
        print("PaintBrush.change_width")