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
        w = self.width
        self.canvas.create_rectangle(x - w / 2, y - w / 2, x + w / 2, y + w / 2, fill = self.color, outline = "")

    def change_color(self, p):
        colors = askcolor(title="Tkinter Color Chooser")
        self.color = colors[1]