import json
import os

class Pet:
    
    type = ""

    @staticmethod
    def load(data_path):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        data_dir = os.path.join(main_dir, data_path)
        data = open(data_dir,)
        
        pet = Pet()
        pet.__dict__ = json.load(data)
        return pet