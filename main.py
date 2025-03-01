import pygame
import os
from image_loader import ImageLoader
from pet import Pet
from pet import Need
import pygame_gui
from views import NeedsGroupView

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

# TODO: ideally, read from a json
def setupPetNeeds():
    food = Need(0, 1, "Feed")
    hygene = Need(0, 2, "Clean")
    playtime = Need(0, 3, "Play")
    
    return [food, hygene, playtime]

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), theme_path="ui/theme.json")

needs = setupPetNeeds()
needsUI = NeedsGroupView(manager, needs)

while running:

    deltaTime = clock.get_rawtime() / 1000

    clickPos = pygame.mouse.get_pos()
    wasClicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            wasClicked = True
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
              needsUI.handleUIEvent(event)

        manager.process_events(event)

    manager.update(deltaTime)

    screen.fill(BACKGROUND_COLOR)

    image_loader = ImageLoader(DATA_FOLDER)

    cat = Pet.instantiate(os.path.join(DATA_FOLDER, DEFAULT_PET))

    screen.blit(cat.sprite[0], (0,0))

    for need in needs:
        need.update(deltaTime)
    needsUI.update()

    manager.draw_ui(screen)
   
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

