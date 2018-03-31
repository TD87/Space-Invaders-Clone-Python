import random, time
from graphics import *

class Prototype_Alien:
    """The base class for the 2 types of aliens"""

    def __init__(self):
        pass

    def draw(self, graphics_window):
        self.sprite.draw(graphics_window)

    def undraw(self):
        self.sprite.undraw()


class Alien(Prototype_Alien):
    """Regular Alien class with a lifespan of 10 seconds. Denoted by # """
    def __init__(self):
        self.type = "regular"
        self.lifespan = 8
        self.spawn_time = time.time()
        self.x = random.randint(0, 7)
        self.y = random.randint(0, 1)
        self.sprite = Text(Point(30 + self.x*20, 40 + self.y*20), "#")
        self.sprite.setSize(20)
        self.sprite.setFill("green")


class Crippled_Alien(Prototype_Alien):
    """Crippled Alien class with lifespan of 5 seconds. Denoted by @ """

    def __init__(self, x, y):
        self.type = "crippled"
        self.lifespan = 5
        self.spawn_time = time.time()
        self.x = x
        self.y = y
        self.sprite = Text(Point(30 + self.x*20, 40 + self.y*20), "@")
        self.sprite.setSize(20)
        self.sprite.setFill("brown")
