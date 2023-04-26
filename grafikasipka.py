from tkinter import *
class DrawingApp:

    def __init__(self,canvas):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.s = 0
        self.m = 0
        self.canvas=canvas


    def prvy(self, x,y):
        if self.s == 0:
            self.x1 = x
            self.y1 = y
            self.s += 1
            self.m += 1


    def druhy(self, x,y):
        if self.s == 1:
            self.x2 = x
            self.y2 = y
            self.s = 0
        self.s = 0

    def kresli(self,px,py, x, y,m):
        if self.s == 0 or self.s == 1:
            self.canvas.delete('stvorec'+str(m))
            self.canvas.delete('vrh'+str(m))
            self.canvas.create_rectangle(px+(x-px)/4, py+(y-py)/2, x-(x-px)/4, y, fill = 'blue', outline = 'blue', tag="stvorec"+str(m))
            points = [px,py+(y-py)/2, x,py+(y-py)/2, px/2+x/2, py]
            self.canvas.create_polygon(points, fill='blue',tag="vrh"+str(m))

