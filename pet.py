import json
import os
from image_loader import ImageLoader

class Pet:

    SPRITE_KEY = "sprite"

    type = ""

    def __init__(self, data_path, dictionary):
        self.__dict__ = dictionary
        loader = ImageLoader(data_path)
        self.sprite = loader.load_image(dictionary[self.SPRITE_KEY], -1, self.spriteScale)

    @staticmethod
    def instantiate(data_path):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        data_full_path = os.path.join(main_dir, data_path)
        data = open(data_full_path,)

        pet = Pet(os.path.dirname(data_full_path), json.load(data))
        return pet
    

class Need:
    def __init__(self, startLevel, cooldown):
        self._cooldown = cooldown
        self.startLevel = startLevel
        self._currentLevel = startLevel

    def _get_remainingTime(self):
        return self._cooldown - (self._currentLevel * self._cooldown)
    
    remainingTime = property(
        fget=_get_remainingTime
    )
    
