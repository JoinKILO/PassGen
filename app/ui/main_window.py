import customtkinter as ctk
from random import choice
import string

class MainWidow(ctk.CTk):
    
    can_resize = False
    alphabet = alphabet = string.ascii_lowercase + string.ascii_uppercase + "0123456789#_$*"
    password = ""
    
    def __init__(self):
        super().__init__()
        
        # # # Main window and option tabview # # #
        ctk.set_default_color_theme("app/assets/themes/midnight.json")
        self.iconbitmap("app/assets/images/icon.ico")
        self.geometry("1240x920")
        self.title("PASSGEN - Password Generator")
        self._set_appearance_mode("system")
        
        # Create Tab Option
        self.tab_option = ctk.CTkTabview(master=self, height=900)
        self.tab_option.add("Опции")
        
        self.tab_option.place(x=933, y=5)
        
        # Switch option resize
        self.switch_resizable = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="Разрешить изменение размера окна", command=self.on_switch_resizable_toggle)
        self.switch_resizable.pack(anchor="w", padx=5, pady=5)
        
        self.resizable(width=False, height=False)

        # # # Tabview help, problems and connect # # #
        self.tab_contact = ctk.CTkTabview(master=self, height=400)
        self.tab_contact.add("Связь")
        self.tab_contact.add("Проблемы")
        self.tab_contact.add("Поддержка")
        
        self.tab_contact.place(x=5, y=5)
        
        # # # Buttons and label # # #
        self.btn_generate = ctk.CTkButton(master=self, text="Генерировать пароль", corner_radius=15, command=self.on_generate_pressed)
        self.btn_copy = ctk.CTkButton(master=self, text="Скопировать пароль", corner_radius=15)
        self.password_label = ctk.CTkLabel(master=self, text="0000000", bg_color="#000080")
        
        self.password_label.place(x=560, y=370)
        self.btn_copy.place(x=590, y=420)
        self.btn_generate.place(x=420, y=420)
        
        
    def on_switch_resizable_toggle(self):
        if self.switch_resizable.get() == 1:
            self.can_resize = True
        else:
            self.can_resize = False
        self.resizable(width=self.can_resize, height=self.can_resize)
    
    def on_generate_pressed(self):
        self.password = ""
        for i in range(8):
            self.password += choice(self.alphabet)
        self.password_label.configure(True, text=self.password)