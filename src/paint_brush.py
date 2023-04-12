# ===============================================================================================
# A paint brush object with adjustable width and color
# ===============================================================================================

from tkinter import *
from src.tool import *
from src.command import DrawPixelCommand
from src.defaults import *
from tkinter.colorchooser import askcolor

class PaintBrush(Tool):
    def __init__(self, image_project, size=default_brush_width, color="black"):
        super().__init__(image_project)
        self.size = size
        self.color = color
    
    def handle_event(self, event):
        if self.active and (event.type == EventType.MOUSEBUTTONDOWN or event.type == EventType.MOUSEMOTION):
            x, y = event.pos
            command = DrawPixelCommand(self, x, y)
            command.execute()

    def change_color(self, color):
        self.color = color

    def change_width(self):
        print("PaintBrush.change_width")