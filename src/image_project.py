from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter.filedialog import asksaveasfilename, askopenfilename
from PIL import Image, ImageTk
from PIL import Image as PilImage, ImageTk

import src.util as Util
from src.paint_brush import PaintBrush
from src.defaults import *
from src.mat_vec import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

class ImageProject:
    def __init__(self, canvas):
        self.canvas = canvas
        self.photo_image = None
        self.orig_pil_image = None
        self.pil_image = None
        self.width = None
        self.height = None

    def new(self):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.pil_image = PilImage.new("RGB", (self.width, self.height), (255, 255, 255))
        self.photo_image = ImageTk.PhotoImage(self.pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)

    def open(self, file_path):
        self.orig_pil_image = PilImage.open(file_path)
        self.pil_image = self.orig_pil_image.copy()
        self.width, self.height = self.pil_image.size
        self.photo_image = ImageTk.PhotoImage(self.pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)

    def save(self, file_path):
        self.pil_image.save(file_path)

    def resize(self, width, height):
        resized_pil_image = self.orig_pil_image.resize((width, height))
        self.pil_image = resized_pil_image.copy()
        self.width, self.height = self.pil_image.size
        self.photo_image = ImageTk.PhotoImage(self.pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
