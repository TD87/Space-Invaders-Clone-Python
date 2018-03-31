from player import *
from graphics import *
from missile import *

class custom_window(GraphWin):
    """Custom Graphics Window that directly reads key presses and moves player
        or places missiles"""

    def __init__(self, title="Graphics Window", width=200, height=200):
        super().__init__(title, width, height)
        self.play_field = Rectangle(Point(15, 25), Point(185, 180))
        self.play_field.draw(self)
        self.player = Player()
        self.player.draw(self)
        self.missile_list = list()
        self.closed = 0
        self.godmode = 0


    """Overloading keypress action"""
    def _onKey(self, event):
        self.keypress_action(event)
        self.lastKey = event.keysym


    """Moving the player or spawning missiles based on keypress"""
    def keypress_action(self, event):
        move = event.char
        if move == 'd' and self.player.getX() < 170.0:
            self.player.move(20, 0)
        elif move == 'a' and self.player.getX() > 30.0:
            self.player.move(-20, 0)
        elif move == ' ' and self.player.getY() > 40.0:
            missile_object = Standard_Missile(self.player.getX(), self.player.getY())
            missile_object.draw(self)
            self.missile_list.append(missile_object)
        elif move == 's' and self.godmode == 0:
            missile_object = Bullet_Missile(self.player.getX(), self.player.getY())
            missile_object.draw(self)
            self.missile_list.append(missile_object)
        elif move == 'q':
            self.close()
            self.closed = 1


        """God mode moves. Essentially allows you to move up and down as well
            and binds bullet missile to e. Unlocked by pressing 0"""
        if move == '0':
            self.godmode = 1
        elif move == 's' and self.godmode == 1 and self.player.getY() < 180.0:
            self.player.move(0, 20)
        elif move == 'w' and self.godmode == 1 and self.player.getY() > 40.0:
            self.player.move(0, -20)
        elif move == 'e' and self.godmode == 1 and self.player.getY() > 40.0:
            missile_object = Bullet_Missile(self.player.getX(), self.player.getY())
            missile_object.draw(self)
            self.missile_list.append(missile_object)
