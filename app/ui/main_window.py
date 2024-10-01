import customtkinter as ctk
from PIL import Image

class MainWidow(ctk.CTk):
    
    can_resize = True
    
    def __init__(self):
        super().__init__()
        
        self.geometry("1240x920")
        self.title("PASSGEN - Password Generator")
        self._set_appearance_mode("system")
        self.resizable(width=False, height=False)
        
        self.tab_option = ctk.CTkTabview(master=self, width=400, height=910)
        self.tab_option.add("Опции")
        
        self.tab_option.pack(anchor="e", padx=10, pady=10)
        
        self.switch_resizable = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="Разрешить изменение размера", command=self.on_can_resizable_toggle)
        self.switch_resizable.pack(anchor="w", padx=5, pady=5)
     
    def on_switch_resizable_toggle(self):
        if self.switch_resizable.get() == 1:
            self.can_resize = True
        else:
            self.can_resize = False
        
        self.resizable(width=self.can_resize, height=self.can_resize)