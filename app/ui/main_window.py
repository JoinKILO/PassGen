import customtkinter as ctk
from random import choice
from app.start import DefaultSettings
import string
import json


class MainWidow(ctk.CTk):
    config = DefaultSettings()
    settings: dict = config.get_settings()
    alphabet: str = string.ascii_lowercase
    length_password: int = 15
    password: str = ""
    cache_history: str = ""
    is_special_symbols: bool = False
    is_digits: bool = False
    is_uppercase: bool = False


    def __init__(self) -> None:
        super().__init__()

        self.resizable(width=False, height=False)

        # # # Главное окно и вкладка опций # # #
        ctk.set_default_color_theme(self.settings["theme"])
        self.iconbitmap(self.settings["icon"])
        self.geometry(self.settings["geometry"])
        self.title(self.settings["title"])
        self._set_appearance_mode(self.settings["appearance_mode"])

        # Создание вкладки опций
        self.tab_option = ctk.CTkTabview(master=self, height=900)
        self.tab_option.add("Опции")

        self.tab_option.place(x=933, y=5)

        # На вкладке опций
        self.option_label = ctk.CTkLabel(
            master=self.tab_option.tab("Опции"), 
            text="Задать атрибуты"
        )
        self.switch_uppercase = ctk.CTkSwitch(
            master=self.tab_option.tab("Опции"), text="A-Z", 
            command=self.update_option
        )
        self.switch_digits = ctk.CTkSwitch(
            master=self.tab_option.tab("Опции"), text="0-9", 
            command=self.update_option
        )
        self.switch_special_symbols = ctk.CTkSwitch(
            master=self.tab_option.tab("Опции"), text="!-]", 
            command=self.update_option
        )

        # Размещение на вкладке опции
        self.option_label.pack(anchor="n")
        self.switch_special_symbols.pack(anchor="w")
        self.switch_digits.pack(anchor="w")
        self.switch_uppercase.pack(anchor="w")

        # # # Вкладка смены темы # # #
        self.tab_theme = ctk.CTkTabview(master=self, height=400)
        self.tab_theme.add("Смена темы")

        # Кнопки смены тем
        self.violet_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Фиолетовый", 
            command=lambda: self.change_theme("violet")
        )
        self.midnight_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Полночь", 
            command=lambda: self.change_theme("midnight")
        )
        self.lavender_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Лаванда", 
            command=lambda: self.change_theme("lavender")
        )
        self.marsh_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Марш", 
            command=lambda: self.change_theme("marsh")
        )
        self.breeze_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Бриз", 
            command=lambda: self.change_theme("breeze")
        )
        self.red_theme = ctk.CTkButton(
            master=self.tab_theme.tab("Смена темы"), 
            text="Красная", 
            command=lambda: self.change_theme("red")
        )

        # Размещение в табе theme
        self.tab_theme.place(x=5, y=5)
        self.violet_theme.pack(pady=5)
        self.midnight_theme.pack(pady=5)
        self.lavender_theme.pack(pady=5)
        self.marsh_theme.pack(pady=5)
        self.breeze_theme.pack(pady=5)
        self.red_theme.pack(pady=5)

        self.restart_message = ctk.CTkLabel(
            master=self,
            text=""
        )
        
        # # # Кнопки, ползунок и метка в главном фрейме # # #
        self.main_frame = ctk.CTkFrame(
            master=self, 
            corner_radius=4
        )
        self.slider_length_password = ctk.CTkSlider(
            master=self.main_frame,
            number_of_steps=30,
            from_=1,
            to=30,
            command=self.update_password_length_slider,
        )
        self.btn_generate = ctk.CTkButton(
            master=self.main_frame,
            text="Генерировать пароль",
            corner_radius=5,
            command=self.on_generate_pressed,
        )
        self.label_password_length = ctk.CTkLabel(
            master=self.main_frame, 
            text="Длина пароля: 15"
        )
        self.btn_copy = ctk.CTkButton(
            master=self.main_frame,
            text="Скопировать пароль",
            corner_radius=5,
            command=self.on_copy_pressed,
        )
        self.password_label = ctk.CTkLabel(
            master=self.main_frame, 
            text="Нажмите на Генерировать пароль"
        )

        # Размещение всех объектов в главном фрейме
        self.restart_message.place(x=455, y=340)
        self.main_frame.place(x=480, y=380)
        self.password_label.pack(anchor="n", padx=5, pady=2)
        self.label_password_length.pack(anchor="n")
        self.slider_length_password.pack(anchor="n", padx=5, pady=2)
        self.btn_generate.pack(anchor="n", padx=5, pady=2)
        self.btn_copy.pack(anchor="n", padx=5, pady=2)

        # # # Фрейм истории # # #
        self.frame_history = ctk.CTkScrollableFrame(master=self, height=465, width=275)
        self.label_history = ctk.CTkLabel(master=self.frame_history, text="")

        # Размещение всех объектов в фрейме истории
        self.frame_history.place(x=5, y=430)
        self.label_history.pack(anchor="n")


    def update_option(self) -> None:
        # Обновить настройки
        self.is_uppercase = self.switch_uppercase.get()
        self.is_digits = self.switch_digits.get()
        self.is_special_symbols = self.switch_special_symbols.get()


    # Генерировать пароль
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


    # Скопировать пароль в буфер обмена
    def on_copy_pressed(self) -> None:
        self.clipboard_clear()  # Очистка необходима, чтобы пароль не сливался с предыдущим
        self.clipboard_append(self.password)


    # Установить длину пароля
    def get_length_password(self) -> int:
        return round(int(self.slider_length_password.get()))


    # Обновить метку при изменении значения ползунка
    def update_password_length_slider(self, _) -> None:
        self.label_password_length.configure(
            text=f"Длина пароля: {round(int(self.slider_length_password.get()))}"
        )
    
    
    def change_theme(self, theme_name: str):
        temp_dict: dict = {}
        with open(self.config.get_file_path(), "r") as read:
            temp_dict = json.load(read)
        
        temp_dict["theme"] = f"app/assets/themes/{theme_name}.json"
        
        with open(self.config.get_file_path(), "w") as write:
            write.write(json.dumps(temp_dict, indent=4))
        
        self.restart_message.configure(False, text="Перезапустите приложение для смены темы")