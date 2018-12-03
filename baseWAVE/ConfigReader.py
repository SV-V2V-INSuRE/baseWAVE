import json
import os

class ConfigReader:
    def __init__(self):
        #load config file
        self_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(self_path,"..")
        self.dict = json.load(config_path)


    def getValue(self, name):
        value = ""
        try:
            value = self.dict[name]
        finally:
            return value