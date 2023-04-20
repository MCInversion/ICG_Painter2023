# ===============================================================================================
# An image project object for containing current image data
# ===============================================================================================

from tkinter import *
import tkinter as tk
import json

#from src.defaults import *
from src.mat_vec import *

class ImageProject():
	
    def __init__(self, canvas):
        self.canvas = canvas
        self.photo_image = None
        with open("src/defaults.json", 'r') as f:
            self.default = json.load(f)
        f.close()
    
    def __configure(self):
        if self.photo_image:
            self.canvas.configure(width=self.photo_image.width(), height=self.photo_image.height())
            self.canvas.create_rectangle(0, 0, self.photo_image.width(), self.photo_image.height(), fill=self.default["image"]["color"])

    def new(self):
        self.canvas.delete('all')
        self.photo_image = tk.PhotoImage(width=self.default["image"]["width"],
                                         height=self.default["image"]["height"])
        self.__configure()
        self.canvas.create_image(0, 0, image=self.photo_image, anchor="nw")

    def open(self, file_path):
        self.photo_image = tk.PhotoImage(file=file_path)
        self.__configure()
        self.canvas.create_image(0, 0, image=self.photo_image, anchor="nw")

    def save(self, file_path):
        self.photo_image.write(file_path, format="png")