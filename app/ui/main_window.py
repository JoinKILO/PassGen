import customtkinter as ctk
import string
from  random import choice

class MainWidow(ctk.CTk):
    
    can_resize = False
    alphabet = string.ascii_lowercase
    length_password = 8
    password = ""
    is_special_symbols = False
    is_digits = False
    is_uppercase = False
    
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
        
        # In option tab
        self.switch_resizable = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="Разрешить изменение размера окна", command=self.on_switch_resizable_toggle)
        
        self.switch_uppercase = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="A-Z", command=self.update_option)
        self.switch_digits = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="0-9", command=self.update_option)
        self.switch_special_symbols = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="!-]", command=self.update_option)
        
        self.switch_resizable.pack(anchor="w")
        self.switch_special_symbols.pack(anchor="w")
        self.switch_digits.pack(anchor="w")
        self.switch_uppercase.pack(anchor="w")
        
        self.resizable(width=False, height=False)

        # # # Tabview help, problems and connect # # #
        self.tab_contact = ctk.CTkTabview(master=self, height=400)
        self.tab_contact.add("Связь")
        self.tab_contact.add("Проблемы")
        self.tab_contact.add("Поддержка")
        
        self.tab_contact.place(x=5, y=5)
        
        # # # Buttons, entry and label in main frame # # #
        self.main_frame = ctk.CTkFrame(master=self, corner_radius=4)
        self.length_password_entry = ctk.CTkEntry(master=self.main_frame, placeholder_text="Длина пароля по умолчанию 8")
        self.btn_generate = ctk.CTkButton(master=self.main_frame, text="Генерировать пароль", corner_radius=15, command=self.on_generate_pressed)
        self.btn_copy = ctk.CTkButton(master=self.main_frame, text="Скопировать пароль", corner_radius=15, command=self.on_copy_pressed)
        self.password_label = ctk.CTkLabel(master=self.main_frame, text="Нажмите на Генерировать пароль")
        
        # Place all objects in main frame
        self.main_frame.place(x=480, y=380)
        self.password_label.pack(anchor="n", padx=5, pady=2)
        self.length_password_entry.pack(anchor="n", padx=5, pady=2)
        self.btn_generate.pack(anchor="n", padx=5, pady=2)
        self.btn_copy.pack(anchor="n", padx=5, pady=2)
    
    
    # Allow resizable
    def on_switch_resizable_toggle(self):
        
        if self.switch_resizable.get() == 1:
            self.can_resize = True
        else:
            self.can_resize = False
        self.resizable(width=self.can_resize, height=self.can_resize)
    
    
    def update_option(self):
        # Update settings
        self.is_uppercase = self.switch_uppercase.get()
        self.is_digits = self.switch_digits.get()
        self.is_special_symbols = self.switch_special_symbols.get()
    
    
    # Generate password
    def on_generate_pressed(self):
        alphabet = list(string.ascii_lowercase)

        if self.is_uppercase:
            alphabet.extend(string.ascii_uppercase)
        if self.is_digits:
            alphabet.extend(string.digits)
        if self.is_special_symbols:
            alphabet.extend("!@#$%^&*()-_=+[]{}|;:,.<>?")

        self.set_length_password()
        self.password = "".join(choice(alphabet) for _ in range(self.length_password))

        if self.length_password <= 30:
            self.password_label.configure(text=self.password)
        else:
            self.password_label.configure(text="Максимальное значение: 30")
    
    
    # Copy password to clipboard
    def on_copy_pressed(self):
        self.clipboard_clear() # Cleaning is necessary so that the password does't merge with the past
        self.clipboard_append(self.password)
    
    
    # Set length password
    def set_length_password(self):
        try:
            self.length_password = int(self.length_password_entry.get())
        except ValueError:
            self.length_password = 8
            self.length_password_entry.delete(0, "end")
    