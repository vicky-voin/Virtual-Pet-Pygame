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
    def __init__(self, startLevel, cooldown, actionString):
        self._cooldown = cooldown
        self.startLevel = startLevel
        self._fulfillLevel = startLevel
        self.actionString = actionString

    @property
    def remainingTimeTillCritical(self):
        return self._fulfillLevel * self._cooldown
    
    @property
    def fulfillPercentage(self):
        return self._fulfillLevel
    
    def fulfill(self):
        self._fulfillLevel = 1

    def update(self, deltaTime):
        self._fulfillLevel -= deltaTime / self._cooldown
        self._fulfillLevel = min(1, max(0, self._fulfillLevel))
    
