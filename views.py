import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class NeedView:

    NEED_STATE_FULL = "@need_button-full"
    NEED_STATE_NEUTRAL = "@need_button-neutral"
    NEED_STATE_CRITICAL = "@need_button-critical"

    VIEW_WIDTH = 100
    VIEW_HEIGHT = 50

    def __init__(self, ui_manager, needObject):
       self._needObject = needObject
       self._button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (self.VIEW_WIDTH, self.VIEW_HEIGHT)),
                                             text= needObject.actionString,
                                             manager=ui_manager)

    def set_position(self, position):
        self._button.set_position(position)

    def update(self):
        targetState = self.NEED_STATE_FULL if self._needObject.fulfillPercentage >= 0.5 else self.NEED_STATE_NEUTRAL
        
        if self._needObject.fulfillPercentage == 0:
            targetState = self.NEED_STATE_CRITICAL

        self._button.change_object_id(ObjectID(class_id=targetState))

    def wasClicked(self, ui_event):
        return ui_event.ui_element == self._button
    
    def viewRect(self):
        return self._button.rect

class NeedsGroupView:

    ELEMENT_SPACING = 20

    def __init__(self,ui_manager, needs):
        self._needs = []
        self.totalViewWidth = 0
        self._screenWidth = ui_manager.get_root_container().get_rect().width

        for need in needs:
            view = NeedView(ui_manager, need)
            self._needs.append((need, view))
            self.totalViewWidth += view.viewRect().width + self.ELEMENT_SPACING

        # Last view shouldn't have spacing at the end
        self.totalViewWidth -= self.ELEMENT_SPACING
        print(self._screenWidth)
        print(self.totalViewWidth)    

    def update(self):
        
        startingPositionX = (self._screenWidth - self.totalViewWidth) / 2 - self._needs[0][1].viewRect().width - self.ELEMENT_SPACING

        for need in self._needs:
            buttonWidth = need[1].viewRect().width
            spacing = self.ELEMENT_SPACING
            yPos = buttonWidth/2 + 50
            buttonPos = (startingPositionX + buttonWidth + spacing, yPos)

            need[1].set_position(buttonPos)
            need[1].update()

            startingPositionX = buttonPos[0]

    def handleUIEvent(self, event):
        clickedNeed = [need for need in self._needs if need[1].wasClicked(event)]
        if clickedNeed:
            clickedNeed[0][0].fulfill()