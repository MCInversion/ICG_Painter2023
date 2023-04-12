# ===============================================================================================
# A base class for tools in the ICG Painter application
# ===============================================================================================

from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self, image_project):
        self.image_project = image_project
        self.active = False
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    @abstractmethod
    def handle_event(self, event):
        pass