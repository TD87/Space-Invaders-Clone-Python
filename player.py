from graphics import *

class Player:
    """The Player Class with basic move functionality"""

    def __init__(self):
        self.sprite = Text(Point(30, 180), "^")
        self.sprite.setSize(36)
        self.sprite.setFill("purple")

    def draw(self, graphics_window):
        self.sprite.draw(graphics_window)

    def getX(self):
        return self.sprite.getAnchor().getX()

    def getY(self):
        return self.sprite.getAnchor().getY()

    def move(self, dx, dy):
        self.sprite.move(dx, dy)
