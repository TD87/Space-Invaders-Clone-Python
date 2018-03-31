from graphics import *

class Scoreboard:
    """Scoreboard class that keeps a count of how many aliens the player has killed"""

    def __init__(self):
        self.score = 0
        self.sprite = Text(Point(215, 35), self.score)
        self.sprite.setSize(20)

    def update_score(self):
        self.score += 1
        self.sprite.setText(self.score)

    def draw(self, graphics_window):
        self.sprite.draw(graphics_window)
