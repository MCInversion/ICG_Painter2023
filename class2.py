

from PIL import ImageGrab
from tkinter import *
class Select_copy:
    def __init__(self, meno, canvas, stav):
        self.meno = meno
        self.c = 0
        self.control=False
        self.x, self.y = 0, 0
        self.n=0
        self.images=[]
        self.canvas=canvas
 
    def sel1(self, e):
        global vyber_x1, vyber_y1
        vyber_x1, vyber_y1 = e.x, e.y
   
    def sel2(self, e):
        global  vyber_x2, vyber_y2, vyber_x1, vyber_y1
        if self.c==0:
            vyber_x2, vyber_y2 = e.x, e.y
            self.canvas.delete('vyber', 'roh')
            self.canvas.create_rectangle(vyber_x1, vyber_y1, vyber_x2, vyber_y2,
                             width=3, dash=(5,3), tag='vyber')
            self.canvas.create_oval(vyber_x2-3, vyber_y2-3,vyber_x2+3, vyber_y2+3,
                       fill='gray', tag='roh')
        else:
            global sirka, vyska, name
            if 250-abs(sirka)/2<=vyber_x1<=250+abs(sirka)/2 and 250-abs(vyska)/2<=vyber_y1<=250+abs(vyska)/2:
                if self.x!=0 and self.y!=0:
                    self.canvas.move(name, e.x-self.x, e.y-self.y)
                self.x= e.x
                self.y=e.y
            else: 
                self.c=0

    def getter(self, widget):
        global vyber_x1, vyber_y1, sirka, vyska
        a=self.canvas.winfo_rootx())
        b=self.canvas.winfo_rooty()
        ImageGrab.grab().crop(
            (a+vyber_x1+2,b+vyber_y1+2,a+vyber_x1+abs(sirka)-2,b+vyber_y1+abs(vyska)-2)).save("em.png")

    def ctrl(self, s):
        self.control=True
    
    def copy(self, s):
        global vyber_x2, vyber_y2, vyber_x1, vyber_y1, sirka, vyska, name 
        if self.control:
            self.c+=1
            sirka=vyber_x1-vyber_x2
            vyska=vyber_y1-vyber_y2
            self.getter(self.canvas)

    def paste(self, s):
        global img, name
        if self.control:
            self.n+=1
            name='k'+str(self.n)+str(self.meno)
            self.images+=[PhotoImage(file='em.png'),]
            self.canvas.create_image(250,250, image=self.images[self.n-1], tag=name)
            self.x, self.y = 0, 0
