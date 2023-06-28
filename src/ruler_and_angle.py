# ===============================================================================================
# Ruler and Angle objects
# ===============================================================================================

from math import *

from tkinter import *
import tkinter as tk
from tkinter.colorchooser import askcolor

class Ruler():
    def __init__(self, canvas, reporting_label):
        self.canvas = canvas
        self.reporting_label = reporting_label
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.dist = None

    def clear(self, p):
        self.reporting_label.config(text='')
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.dist = None
 
    def process_click(self, p):

        if self.x1 is None:
            self.x1 = p.x
            self.y1 = p.y

        elif self.x2 is None:
            self.x2 = p.x
            self.y2 = p.y
            self.measure_and_report()

        else:
            self.clear(None)
            self.x1 = p.x
            self.y1 = p.y

    def measure_and_report(self):
        self.dist = round(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5, 2)
        self.reporting_label.config(text=f'Ruler measure: {self.dist} px')


class Angle():
    def __init__(self, canvas, reporting_label):
        self.canvas = canvas
        self.reporting_label = reporting_label
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.x3 = None
        self.y3 = None
        self.angl = None

    def clear(self, p):
        self.reporting_label.config(text='')
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.x3 = None
        self.y3 = None
        self.angl = None
 
    def process_click(self, p):

        if self.x1 is None:
            self.x1 = p.x
            self.y1 = p.y

        elif self.x2 is None:
            self.x2 = p.x
            self.y2 = p.y

        elif self.x3 is None:
            self.x3 = p.x
            self.y3 = p.y
            self.measure_and_report()

        else:
            self.clear(None)
            self.x1 = p.x
            self.y1 = p.y
        

    def measure_and_report(self):
        self.angl = round(degrees(acos(((self.x2-self.x1)*(self.x2-self.x3)+(self.y2-self.y1)*(self.y2-self.y3))/(((self.x2-self.x1)**2+(self.y2-self.y1)**2)*((self.x2-self.x3)**2+(self.y2-self.y3)**2))**0.5)),2)
        self.reporting_label.config(text=f'Angle measure: {self.angl}°')
