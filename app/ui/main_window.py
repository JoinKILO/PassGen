import customtkinter as ctk
import string
from  random import choice

class MainWidow(ctk.CTk):
    
    can_resize = False
    alphabet = string.ascii_lowercase
    length_password = 8
    password = ""
    cache_history = ""
    is_special_symbols = False
    is_digits = False
    is_uppercase = False
    
    
    def __init__(self) -> None:
        super().__init__()
        
        self.resizable(width=False, height=False)
        
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
        self.switch_uppercase = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="A-Z", command=self.update_option)
        self.switch_digits = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="0-9", command=self.update_option)
        self.switch_special_symbols = ctk.CTkSwitch(master=self.tab_option.tab("Опции"), text="!-]", command=self.update_option)
        
        self.switch_special_symbols.pack(anchor="w")
        self.switch_digits.pack(anchor="w")
        self.switch_uppercase.pack(anchor="w")
        

        # # # Tabview help, problems and connect # # #
        self.tab_contact = ctk.CTkTabview(master=self, height=400)
        self.tab_contact.add("Связь")
        self.tab_contact.add("Проблемы")
        self.tab_contact.add("Поддержка")
        
        self.tab_contact.place(x=5, y=5)
        
        # # # Buttons, slider and label in main frame # # #
        self.main_frame = ctk.CTkFrame(master=self, corner_radius=4)
        self.slider_length_password = ctk.CTkSlider(master=self.main_frame, number_of_steps=30, from_=1, to=30, command=self.update_password_length_slider)
        self.btn_generate = ctk.CTkButton(master=self.main_frame, text="Генерировать пароль", corner_radius=15, command=self.on_generate_pressed)
        self.label_password_length = ctk.CTkLabel(master=self.main_frame, text="Длинна пароля: 15")
        self.btn_copy = ctk.CTkButton(master=self.main_frame, text="Скопировать пароль", corner_radius=15, command=self.on_copy_pressed)
        self.password_label = ctk.CTkLabel(master=self.main_frame, text="Нажмите на Генерировать пароль")
        
        # Place all objects in main frame
        self.main_frame.place(x=480, y=380)
        self.password_label.pack(anchor="n", padx=5, pady=2)
        self.label_password_length.pack(anchor="n")
        self.slider_length_password.pack(anchor="n", padx=5, pady=2)
        self.btn_generate.pack(anchor="n", padx=5, pady=2)
        self.btn_copy.pack(anchor="n", padx=5, pady=2)
        
        # # # History Frame # # #
        self.frame_history = ctk.CTkScrollableFrame(master=self, height=465, width=275)
        self.label_history = ctk.CTkLabel(master=self.frame_history, text="")
        
        # Place all objects in history frame
        self.frame_history.place(x=5, y=430)
        self.label_history.pack(anchor="n")
    
    
    def update_option(self) -> None:
        # Update settings
        self.is_uppercase = self.switch_uppercase.get()
        self.is_digits = self.switch_digits.get()
        self.is_special_symbols = self.switch_special_symbols.get()
    
    
    # Generate password
    def on_generate_pressed(self) -> None:
        alphabet = list(string.ascii_lowercase)
        
        if self.is_uppercase:
            alphabet.extend(string.ascii_uppercase)
        if self.is_digits:
            alphabet.extend(string.digits)
        if self.is_special_symbols:
            alphabet.extend("!@#$%^&*()-_=+[]{}|;:,.<>?")

        self.length_password = self.get_length_password()
        self.password = "".join(choice(alphabet) for _ in range(self.length_password))

        if self.length_password <= 30:
            self.cache_history += "\n" + self.password
            self.password_label.configure(text=self.password)
            self.label_history.configure(text=self.cache_history)
        else:
            self.password_label.configure(text="Максимальное значение: 30")
    
    
    # Copy password to clipboard
    def on_copy_pressed(self) -> None:
        self.clipboard_clear() # Cleaning is necessary so that the password does't merge with the past
        self.clipboard_append(self.password)
    
    
    # Set length password
    def get_length_password(self) -> int:
        return round(int(self.slider_length_password.get()))
    
    # Update label when slider value change
    def update_password_length_slider(self, slider) -> None: # Need 2 arguments
        self.label_password_length.configure(text=f"Длинна пароля: {round(int(self.slider_length_password.get()))}")
