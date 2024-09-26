from customtkinter import *
from PIL import Image

# Инициализация переменных
can_resizable = False
theme = "themes/violet.json"
appearance = "system"

# Настройки главного окна
root = CTk()
root.iconbitmap("images\icon.ico")
root.geometry("1400x920")
root.title("PASSGEN - Password generator")
root.resizable(width=False, height=False)

set_appearance_mode(appearance)
set_default_color_theme(theme)


# Когда свитч переключается
def on_resize_option_changed():
    if resize_option.get() == 0: # Если свитч выключен запретить изменение окна
        can_resizable = False
    elif resize_option.get() == 1: # Если свитч включен разрешить изменение окна
        can_resizable = True
    root.resizable(width=can_resizable, height=can_resizable)


# Создание табов и расположение их справа
tabs = CTkTabview(master=root, width=400, height=900, anchor="w")
tabs.add("Настройки")
tabs.add("Темы  ")

# Создаем свитч в табе настроек
resize_option = CTkSwitch(tabs.tab("Настройки"), text="Разрешить изменение окна", 
                            command=on_resize_option_changed)

# Расположение экземпляров
resize_option.pack(anchor="n")
tabs.pack(anchor="e", pady=20, padx=20)

# Запуск бесконечного цикла
root.mainloop()
