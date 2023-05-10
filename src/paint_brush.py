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
        self.snap = False
        self.x0 = 0
        self.y0 = 0
 
    def draw_pixel(self, p):
        x, y = p.x, p.y
        r = int(self.width / 2)
        if not self.snap:
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color, outline="")
            return
        dx = x - self.x0
        dy = y - self.y0
        if abs(dx) < dy:
            self.canvas.create_oval(self.x0 - r, self.y0 - r + dy, self.x0 + r, self.y0 + r + dy, fill=self.color, outline='')
        if abs(dy) < dx:
            self.canvas.create_oval(self.x0 - r + dx, self.y0 - r, self.x0 + r + dx, self.y0 + r, fill=self.color, outline='')
        if abs(dx) < -dy:
            self.canvas.create_oval(self.x0 - r, self.y0 - r + dy, self.x0 + r, self.y0 + r + dy, fill=self.color, outline='')
        if abs(dy) < -dx:
            self.canvas.create_oval(self.x0 - r + dx, self.y0 - r, self.x0 + r + dx, self.y0 + r, fill=self.color, outline='')
      
    def assign_initial(self, p):
        if self.x0 == 0 and self.y0 == 0:
            self.x0, self.y0 = p.x, p.y
        else:
            self.x0, self.y0 = 0, 0

    def change_color(self, p):
        colors = askcolor(title="Tkinter Color Chooser")
        self.color = colors[1]

    def change_width(self, p):
        print("PaintBrush.change_width")

    
