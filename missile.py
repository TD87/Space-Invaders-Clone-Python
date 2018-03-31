from graphics import *
import time

class Missile:
    """Base Missile Template"""
    def __init__(self):
        pass

    def draw(self, graphics_window):
        self.sprite.draw(graphics_window)

    def undraw(self):
        self.sprite.undraw()

    def move(self):
        pass

    def getX(self):
        return int((self.sprite.getAnchor().getX() - 30) / 20)

    def getY(self):
        return int((self.sprite.getAnchor().getY() - 40) / 20)


class Standard_Missile(Missile):
    """Standard Missile that moves a block a second. Denoted by i """
    def __init__(self, x_coordinate, y_coordinate):
        self.type = "standard"
        self.start_time = time.time()
        self.sprite = Text(Point(x_coordinate, y_coordinate - 20), "i")
        self.sprite.setSize(15)
        self.sprite.setFill("blue")

    def move(self):
        self.sprite.move(0, -20)


class Bullet_Missile(Missile):
    """Bullet Missile that moves 2 blocks a second. Denoted by I """

    def __init__(self, x_coordinate, y_coordinate):
        self.type = "bullet"
        self.start_time = time.time()
        self.sprite = Text(Point(x_coordinate, y_coordinate - 20), "I")
        self.sprite.setSize(15)
        self.sprite.setFill("red")

    def move(self):
        self.sprite.move(0, -40)
