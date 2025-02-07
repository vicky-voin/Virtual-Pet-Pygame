import pygame
import os

class ImageLoader:

    def __init__(self, datapath):
        self._main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._data_dir = os.path.join(self._main_dir, datapath)

    def load_image(self, name, colorkey=None, scale=1):
        fullname = os.path.join(self._data_dir, name)
        image = pygame.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pygame.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = pygame.Color(255,255,255,255)
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()
