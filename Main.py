import time
from custom_window import *
from alien import *
from scoreboard import *

class Engine:
    def __init__(self):
        """Create graphics window, scoreboard, position grid and alien list"""
        self.graphics_window = custom_window("Space Invaders", 300, 300)
        self.scoreboard = Scoreboard()
        self.alien_list = list()
        self.positions = list()
        for i in range(8):
            self.positions.append([0] * 8)
        self.start_time = time.time()
        self.alien_rate = 5
        self.missile_rate = 0.5
        self.alien_num = 4


    def run(self):
        """Run game logic"""
        self.start_time = time.time() - self.alien_rate
        self.scoreboard.draw(self.graphics_window)

        """Infinite loop start"""
        while not self.graphics_window.closed:
            """Checks for keypresses on graphics window and update it accordingly"""
            self.graphics_window.update_idletasks()
            self.graphics_window.update()

            """Updates missiles in the missile list if they haven't been updated for 1 second"""
            for missile in self.graphics_window.missile_list:
                if time.time() >= missile.start_time + self.missile_rate and missile.getY() <= 0:               #Missile reached end of play field
                    self.remove_missile(missile)
                elif time.time() >= missile.start_time + self.missile_rate and missile.type == "bullet" and missile.getY() <= 1:
                    self.remove_missile(missile)
                elif time.time() >= missile.start_time + self.missile_rate:                                     #Missile needs to be moved
                    missile.move()
                    missile.start_time = time.time()
                    try:
                        pos = self.positions[missile.getY()][missile.getX()]
                        if pos != 0 and pos.type == "regular":                                        #Missile collided with alien
                            self.remove_alien(self.positions[missile.getY()][missile.getX()])
                            self.remove_missile(missile)
                            self.scoreboard.update_score()
                            if missile.type == "bullet":                                              #Check if missile is Bullet type
                                self.insert_alien(Crippled_Alien(missile.getX(), missile.getY()))
                    except:
                        self.remove_missile(missile)                                                  #Missile went out of play field

            """Spawns alien if it has been 10 seconds since last one spawned"""
            if time.time() >= self.start_time + self.alien_rate:
                for x in range(self.alien_num):                                                       #Can spawn as many aliens as you want at a time
                    if len(self.alien_list) < 16:
                        alien_to_insert = object()
                        while True:
                            alien_to_insert = Alien()
                            if self.positions[alien_to_insert.y][alien_to_insert.x] == 0:
                                break
                        self.insert_alien(alien_to_insert)
                        self.start_time = time.time()

            """Despawns alien if it has reached the end of it's lifespan"""
            for alien_object in self.alien_list:
                if time.time() >= alien_object.spawn_time + alien_object.lifespan:
                    self.remove_alien(alien_object)

        """Infinite loop end"""


    def insert_alien(self, alien_object):
        self.positions[alien_object.y][alien_object.x] = alien_object
        alien_object.draw(self.graphics_window)
        self.alien_list.append(alien_object)


    def remove_alien(self, alien_object):
        self.positions[alien_object.y][alien_object.x] = 0
        alien_object.undraw()
        self.alien_list.remove(alien_object)


    def remove_missile(self, missile):
        missile.undraw()
        self.graphics_window.missile_list.remove(missile)


if __name__ == '__main__':
    engine = Engine()
    engine.run()
