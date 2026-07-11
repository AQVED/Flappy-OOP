from pygame import *
from sprite import Sprite


class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= 5
        if keys[K_DOWN]:
            self.rect.y += 5
            