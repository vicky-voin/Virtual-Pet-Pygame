import pygame
import os
from image_loader import ImageLoader
from pet import Pet

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
BACKGROUND_COLOR = "pink"
DATA_FOLDER = "data"
DEFAULT_PET =  "pet_cat.json"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    image_loader = ImageLoader(DATA_FOLDER)

    cat = Pet.instantiate(os.path.join(DATA_FOLDER, DEFAULT_PET))

    screen.blit(cat.sprite[0], (0,0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()