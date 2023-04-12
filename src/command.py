# ===============================================================================================
# A collection of commands for the ICG Painter application
# ===============================================================================================

import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class NewImageCommand(Command):
    def __init__(self, image_project):
        self.image_project = image_project
    
    def execute(self):
        self.image_project.new()

class OpenFileCommand(Command):
    def __init__(self, filetypes):
        self.filetypes = filetypes

    def execute(self, image_project):
        file_path = tk.filedialog.askopenfilename(filetypes=self.filetypes)
        if file_path:
            image_project.open(file_path)

class SaveFileCommand(Command):
    def __init__(self, image_project):
        self.image_project = image_project

    def execute(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_project.save(file_path)

class QuitCommand(Command):
    def __init__(self, parent):
        self.parent = parent
    
    def execute(self):
        self.parent.quit()

class ChangeColorCommand(Command):
    def __init__(self, paint_brush, color):
        self.paint_brush = paint_brush
        self.color = color
    
    def execute(self):
        self.paint_brush.change_color(self.color)

class DrawPixelCommand(Command):
    def __init__(self, paint_brush, x, y):
        self.paint_brush = paint_brush
        self.x = x
        self.y = y
    
    def execute(self):
        self.paint_brush.draw_pixel(self.x, self.y)

class ActivateToolCommand(Command):
    def __init__(self, tool):
        self.tool = tool
    
    def execute(self):
        self.tool.activate()

class DeactivateToolCommand(Command):
    def __init__(self, tool):
        self.tool = tool
    
    def execute(self):
        self.tool.deactivate()