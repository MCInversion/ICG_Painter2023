# ===============================================================================================
# A collection of wrappers for Tkinter UI classes and the relevant bindings
# ===============================================================================================

from tkinter import *

class CommandMenu(Menu):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.parent = parent
		
	def add_command_with_binding(self, label, command, accelerator = None):
		self.add_command(label = label, command = command.execute)
		if accelerator is not None:
			self.parent.bind(accelerator, command.execute)


def add_tool_button(toolbar_frame, tool, tool_icon_img, **button_kwargs):
	button = Button(master = toolbar_frame, image = tool_icon_img, **button_kwargs)
	button.image = tool_icon_img

	def activate_tool():
		tool.activate()
		button.configure(relief = 'sunken')
	
	def deactivate_tool():
		tool.deactivate()
		button.configure(relief = 'raised')
	
	button.configure(command = activate_tool)
	tool.deactivate = deactivate_tool
	
	button.pack(side='left')