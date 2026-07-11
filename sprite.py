from pygame import *

class Sprite:
    def __init__(self,x,y,w,h,color='red',img=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = Rect(self.x,self.y,self.w,self.h)
        self.color = color
        if img is not None:
            self.img = image.load(img)
            self.img = transform.smoothscale(self.img, (self.w, self.h))
            self.rect = self.img.get_rect()

    def draw(self,surface):
        if hasattr(self, 'img'):
            surface.blit(self.img, (self.rect.x, self.rect.y))
        else:
            draw.rect(surface,self.color, self.rect)

    def collide(self, other):
        return self.rect.colliderect(other.rect)