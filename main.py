import pygame
from image_loader import ImageLoader

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
BACKGROUND_COLOR = "pink"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

def draw_cat(image_loader):
    catImage = image_loader.load_image("Cat4.png", -1, 15)
    return catImage

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    image_loader = ImageLoader("data")

    cat = draw_cat(image_loader)

    screen.blit(cat[0], (0,0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()