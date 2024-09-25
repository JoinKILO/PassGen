from customtkinter import *
from PIL import Image

# Инициализация переменных
can_resizable = False

# Настройки главного окна
root = CTk()
root.iconbitmap("images\icon.ico")
root.geometry("1400x920")
root.title("PASSGEN - Password generator")
root.resizable(width=False, height=False)

# Временная тема
set_default_color_theme("blue")

# Возможно стоит возвести всё в класс Option В котором будут храниться настройки приложения
# Когда свитч переключается
def on_resize_option_changed():
    if resize_option.get() == 0: # Если свитч выключен запретить изменение окна
        can_resizable = False
        root.resizable(width=can_resizable, height=can_resizable)
    elif resize_option.get() == 1: # Если свитч включен разрешить изменение окна
        can_resizable = True
        root.resizable(width=can_resizable, height=can_resizable)

# Создание табов и расположение их справа
tabs = CTkTabview(master=root, width=400, height=900, anchor="w")
tabs.add("Option")

# Создаем свитч в Option табе
resize_option = CTkSwitch(tabs.tab("Option"), text="Разрешить изменение окна", 
                          command=on_resize_option_changed)

# Расположение экземпляров
resize_option.pack(anchor="n")
tabs.pack(anchor="e", pady=20, padx=20)

# Запуск бесконечного цикла
root.mainloop()
