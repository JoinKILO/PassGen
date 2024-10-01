import customtkinter as ctk
from PIL import Image

class MainWidow(ctk.CTk):
    
    can_resize = True
    
    def __init__(self):
        super().__init__()
        
        self.geometry("1240x920")
        self.title("PASSGEN - Password Generator")
        self._set_appearance_mode("system")
        
        self.tab_option = ctk.CTkTabview(master=self)
        self.tab_option.add("Опции")
        
        self.tab_option.pack(anchor="e", padx=10, pady=10)
        
        self.can_resizable = ctk.CTkRadioButton(master=self.tab_option.tab("Опции"), text="Разрешить изменение размера")
        self.can_resizable.pack(anchor="w", padx=5, pady=5)
        
        self.resizable(width=False, height=False)
     
    def on_can_resizable_toggle(self):
        pass
        