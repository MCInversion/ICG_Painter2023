# ===============================================================================================
# A collection of wrappers for Tkinter UI classes and the relevant bindings
# ===============================================================================================

from tkinter import *

class CommandMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
    def add_command_with_binding(self, label, command, accelerator = None):
        self.add_command(label = label, command = command.execute())
        if accelerator is not None:
            self.bind_all(accelerator, lambda: command.execute())


def add_tool_button(toolbar_frame, tool_class, **button_kwargs):
    button = Button(master = toolbar_frame, **button_kwargs)
    
    def activate_tool():
        tool_class.activate()
        button.configure(relief = 'sunken')
    
    def deactivate_tool():
        tool_class.deactivate()
        button.configure(relief = 'raised')
    
    button.configure(command = activate_tool)
    tool_class.deactivate = deactivate_tool
    
    button.pack(side='left')