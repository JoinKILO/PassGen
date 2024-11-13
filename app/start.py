import json
import os

class DefaultSettings:
    file_path = "app/assets/themes/config.json"
    
    def get_settings(self) -> dict:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as read:
                return json.load(read)
        else:
            default_settings = {
                "title": "PASSGEN - Генератор паролей",
                "geometry": "1240x920",
                "theme": "app/assets/themes/lavender.json",
                "icon": "app/assets/images/icon.ico",
                "appearance_mode": "dark"
            }
            with open(self.file_path, "w") as write:
                json.dump(default_settings, write)
                