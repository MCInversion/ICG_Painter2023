# ===============================================================================================
# This is the main application class for the ICGPainter Tkinter application.
# ===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.colorchooser import askcolor
import json

import src.util as Util
from src.paint_brush import PaintBrush
#from src.defaults import *
from src.image_project import *

global brush_icon_image

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        with open("src/defaults.json", 'r') as f:
            self.default = json.load(f)
        f.close()
            
        self.parent = parent
        self.parent.geometry("{}x{}".format(self.default["image"]["width"], self.default["image"]["height"]))

        self.toolbar_frame = tk.Frame(self.parent)
        self.toolbar_frame.pack(side="top", fill="x")

        brush_icon_image = PhotoImage(file=r"res\Brush.png")
        self.brush_button = Button(self.toolbar_frame, image=brush_icon_image)
        self.brush_button.image = brush_icon_image
        self.brush_button.pack(side="left")

        self.canvas = Canvas(self.parent, bg = self.default["image"]["color"], height = self.default["image"]["height"], width = self.default["image"]["width"],highlightthickness=0)
        self.canvas.place(x=0, y=self.default["toolbar"]["height"])

        self.image_project = ImageProject(self.canvas)
        self.image_project.new()

        self.brush = PaintBrush(self.canvas, self.default["brush"]["color"], self.default["brush"]["width"])
        self.brush_button.bind('<ButtonPress-1>', self.brush.change_width)

        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.filemenu.add_command(label="New", command=self.image_project.new)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Settings", command=self.set_default)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        self.canvas.bind('<ButtonPress-1>', self.brush.draw_pixel) # bind left button to self.brush.draw_pixel
        self.canvas.bind('<B1-Motion>', self.brush.draw_pixel) # bind mouse move to self.brush.draw_pixel         
        self.parent.bind('<ButtonPress-2>', self.brush.change_color) # bind scroll wheel click to colorpicker

    def open_file(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("PNG Image files", "*.png;")])
        if file_path:
            self.image_project.open(file_path)

    def save_file(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image_project.save(file_path)
    # methods for creating components
    def make_component(self,frame,index,subject,value,row,collum):
        #creanting component
        label = Label(frame, text=subject+" "+value, fg=self.default["text"]["dark_color"])
        label.configure(
            bg="#121212", 
            pady=5, 
            font=(self.default["text"]["name"],self.default["text"]["size"],"bold")
        )
        entry = Entry(frame, width=10,justify="center", insertbackground=self.default["text"]["dark_color"])
        entry.configure(
            bg="#252525", 
            fg=self.default["text"]["dark_color"],
            font=(self.default["text"]["name"],self.default["text"]["size"]),
            borderwidth=0,
            highlightthickness=0,
            )
        entry.insert(0,self.default[subject][value])
        #adding feaures to components
        entry.bind("<Return>",lambda event: self.update_value(index,subject,value))
        entry.bind("<MouseWheel>", lambda event: self.scroll_change(index,subject,value,event))
        if value == "color":
            entry.bind("<Button-1>",lambda event: self.color_picker(index,subject))
        self.entry.append(entry)
        button = Button(frame, text="set", command=lambda index=index,subject=subject,value=value: self.update_value(index,subject,value))
        button.configure(bg="#1a1a1a",
                         fg=self.default["text"]["dark_color"], 
                         font=(self.default["text"]["name"],self.default["text"]["size"]-2),
                         borderwidth=0,
                         highlightthickness=0,
                         padx=4)
    
        #place component on grid
        label.grid(row=row, column=collum, padx=(120,200))
        entry.grid(row=row+1, column=collum, padx=(110,200))
        button.grid(row=row+1, column=collum,padx=(0,0))


    # methods for popup window for setting default parameters
    def color_picker(self,index,subject):
        colors = askcolor(title="Tkinter Color Chooser")
        if colors[1]!=None:
            self.default[subject]["color"] = colors[1]
            self.entry[index].delete(0,END) #delete text from entry box
            self.entry[index].insert(0, self.default[subject]["color"]) 
    def scroll_change(self,index,subject,value,event):
        #when mouse wheel is scrolled, change value of entry box or label depending on subject and value specified
        if type(self.default[subject][value]) == int:
            temp = int(self.entry[index].get())
            if event.delta > 0: #upwards scrolled
                    temp += 1
            else: #downwards scrolled
                    temp -= 1
            self.entry[index].delete(0,END)#delete text from entry box 
            self.entry[index].insert(0,str(temp)) #insert text into entry box
    def update_value(self,index,subject, value):
        #testing for int input
        if self.entry[index].get().isdigit():
            if int(self.entry[index].get()) != self.default[subject][value]:
                self.default[subject][value] = int(self.entry[index].get())
        elif self.entry[index].get() != self.default[subject][value]:
                self.default[subject][value] = self.entry[index].get()
        with open("src/defaults.json", 'w') as f:
            json.dump(self.default,f,indent=4)
        f.close()
        #real time update of new parameter
        #self.parent.geometry("{}x{}".format(self.default["image"]["width"], self.default["image"]["height"]))
        #self.canvas.configure(bg = self.default["image"]["color"], height = self.default["image"]["height"], width = self.default["image"]["width"],highlightthickness=0)
    def show_settings(self,subject):
        #delete previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.entry = []
        #create current content
        header = Label(self.main_frame,text=subject.capitalize()+" settings")
        header.configure(
            fg=self.default["text"]["dark_color"], 
            bg="#111111",
            font=(self.default["text"]["name"],self.default["text"]["size"]+5,"bold")
        )
        header.grid(row=0,column=0,pady=10,padx=(0,70))
        for index,value in enumerate(self.default[subject]):
           self.make_component(self.main_frame,index,subject,value,1+index*2,0)
    def set_default(self):
        self.setting_window = Toplevel(root, bg="#121212")
        self.setting_window.geometry("500x400")
        self.setting_window.title("Settings")

        # left navbar 
        left_navbar = Frame(self.setting_window,bg="#1a1a1a")
        left_navbar.grid(row=0, column=0, sticky='nsew')
        left_navbar.grid_columnconfigure(0, weight=1, minsize=100)
        left_navbar.grid_rowconfigure(0, weight=1, minsize=400)
        # main frame 
        self.main_frame = Frame(self.setting_window,bg="#121212",pady=20)
        self.main_frame.grid(row=0, column=1, sticky='nsew')
        self.main_frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.main_frame.pack_propagate(False)

        
        # buttons div
        buttons_group = Frame(left_navbar,bg="#1a1a1a")
        buttons_group.grid(row=0, column=0,padx=20, pady=20)
        
        # buttons for default settings
        
        buttons = []
        for index, parameter in enumerate(self.default["settings"]["values"]):
            button = Button(buttons_group, text=parameter.capitalize() + " Settings", command=lambda parameter=parameter: self.show_settings(parameter))
            button.configure(**self.default["settings"]["nav_button_style"])
            buttons.append(button)
            buttons[index].grid(row=index, column=0, padx=10, pady=5)


        #default setting from start up
        self.show_settings("image")



if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("res/ICGIcon.ico")
    root.title("Painter")

    MainApplication(root).pack(side = "top", fill = "both", expand = True)
    root.mainloop()