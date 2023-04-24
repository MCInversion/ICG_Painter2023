from tkinter import *
import tkinter as tk
from src.defaults import *


class Symmetry():
    def __init__(self, x, y, a, canvas, color):
        self.x = x
        self.y = y
        self.a = a
        self.canvas = canvas
        self.color = color

    def kresli(self, typ):
        if typ == 'normal':
            self.canvas.create_oval(self.x - self.a, self.y - self.a, self.x + self.a, self.y + self.a, fill=self.color, outline='')
            self.canvas.create_oval(default_img_width - self.x - self.a, self.y - self.a, default_img_width - self.x + self.a, self.y + self.a, fill=self.color, outline='')
            self.canvas.create_oval(self.x - self.a, default_img_height - self.y - self.a, self.x + self.a, default_img_height - self.y + self.a, fill=self.color, outline='')
            self.canvas.create_oval(default_img_width - self.x - self.a, default_img_height - self.y - self.a, default_img_width - self.x + self.a, default_img_height - self.y + self.a, fill=self.color, outline='')
        elif typ == 'horizontal':
            self.canvas.create_oval(self.x - self.a, self.y - self.a, self.x + self.a, self.y + self.a, fill=self.color, outline='')
            self.canvas.create_oval(self.x - self.a, default_img_height - self.y - self.a, self.x + self.a, default_img_height - self.y + self.a, fill=self.color, outline='')
        elif typ == 'vertical':
            self.canvas.create_oval(self.x - self.a, self.y - self.a, self.x + self.a, self.y + self.a, fill=self.color, outline='')
            self.canvas.create_oval(default_img_width - self.x - self.a, self.y - self.a, default_img_width - self.x + self.a, self.y + self.a, fill=self.color, outline='')

