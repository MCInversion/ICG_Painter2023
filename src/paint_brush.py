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
        self.tool = 'eraser'
 
    def draw_pixel(self, p):
        x, y = p.x, p.y
        r = int(self.width / 2)
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color, outline="")

    def change_color(self, p):
        colors = askcolor(title="Tkinter Color Chooser")
        self.color = colors[1]

    def change_width(self, p):
        print("PaintBrush.change_width")
        
    def change_tool(self, tool):
        self.tool = tool
        if tool == 'eraser':  
            self.canvas.bind('<B1-Motion>', self.erase)
            self.canvas.bind('<ButtonPress-1>', self.erase)

            

    def erase(self, event):
        if self.tool == 'eraser':
            fill_color = self.canvas.cget('background')
            x1 = event.x - self.eraser_size
            y1 = event.y - self.eraser_size
            x2 = event.x + self.eraser_size
            y2 = event.y + self.eraser_size
            self.canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline='')

