import csv
import os
import sys

class Locale():
    language = "app\data\lang.csv"
    
    def get_localization(self) -> None:
        with open(self.language, 'r') as lang:
            file = csv.DictReader(self.language)
            
        return file
print('class passed')
