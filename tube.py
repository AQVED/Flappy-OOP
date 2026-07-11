from pygame import *
from sprite import Sprite

class Tube(Sprite):
    def move(self):
        self.rect.x -= 5
        