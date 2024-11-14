import json
import os

class DefaultSettings:
    """
        Ищет файл по пути <app/data/config.json>. Если есть то проверяет, меньше ли он 5 
        стандартных параметров. Если да то записывает значения по умолчанию, иначе возвращает 
        словарь с параметрами из файла
    """
    
    file_path = "app/data/config.json"
    
    def get_settings(self) -> dict:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as read:
                settings = json.load(read)
            
            if len(settings) < 5:
                settings = self._reset_settings()
        else:
            settings = self._reset_settings()
        
        return settings
            
    
    # Сброс значений по умолчанию
    def _reset_settings(self) -> dict:
        default_settings = {
            "title": "PASSGEN - Генератор паролей",
            "geometry": "1240x920",
            "theme": "app/assets/themes/lavender.json",
            "icon": "app/assets/images/icon.ico",
            "appearance_mode": "dark"
        }
        
        with open(self.file_path, "w") as write:
            json.dump(default_settings, write, indent=4)  # Добавлено форматирование для читаемости

        return default_settings
    
    
    def get_file_path(self) -> str:
        return self.file_path