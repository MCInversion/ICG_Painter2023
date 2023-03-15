# ===============================================================================================
# A paint brush object with adjustable width and color
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintBrush():
    def __init__(self, img, color, width):
        self.color = color
        self.width = width
        self.img = img
 
    def __in_image(self, x, y):
        return ((x >= 0) and (x < self.img.photo_image.width()) and \
                (y >= 0) and (y < self.img.photo_image.height()))

    def draw_pixel(self, p):
        x, y = p.x, p.y
        r = int(self.width / 2)
        for dx in range(-r,+r):
            for dy in range(-r,+r):
                if ((dx**2 + dy**2 <= r**2) and self.__in_image(x+dx, y+dy)):
                    self.img.photo_image.put(self.color, to=(x+dx, y+dy))

    def change_color(self, p):
        colors = askcolor(title="Tkinter Color Chooser")
        self.color = colors[1]