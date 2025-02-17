import pygame
import os
from image_loader import ImageLoader
from pet import Pet
from pet import Need

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

def setupPetNeeds():
    food = Need(0, 1, "Feed")
    hygene = Need(0, 2, "Clean")
    playtime = Need(0, 3, "Play")
    
    return [food, hygene, playtime]

needs = setupPetNeeds()

while running:

    deltaTime = clock.get_rawtime() / 1000

    clickPos = pygame.mouse.get_pos()
    wasClicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            wasClicked = True

    screen.fill(BACKGROUND_COLOR)

    image_loader = ImageLoader(DATA_FOLDER)

    cat = Pet.instantiate(os.path.join(DATA_FOLDER, DEFAULT_PET))

    screen.blit(cat.sprite[0], (0,0))

    previousXPosition = 0

    #TODO: refactor the below loop, perhaps move the functionality into the Need class
    for need in needs:
        need.update(deltaTime)
        targetColor = "green" if need.fulfillPercentage >= 0.5 else "white"
        if need.fulfillPercentage == 0:
            targetColor = "red"

        circleSize = 100
        spacing = 20
        yPos = circleSize/2 + 50
        circlePos = (previousXPosition + circleSize + spacing, yPos)
        circleArea = pygame.draw.circle(screen, targetColor, circlePos, circleSize / 2)

        if circleArea.collidepoint(clickPos[0], clickPos[1]) and wasClicked:
             need.fulfill()

        if pygame.font:
            font = pygame.font.Font(None, 24)

            text = font.render(f"{need.actionString}", True, (10, 10, 10))
            textpos = text.get_rect(centerx=circlePos[0], y=circlePos[1])

            screen.blit(text, textpos)

        previousXPosition = circlePos[0]

   
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

