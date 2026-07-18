from pygame import event, key, display, time, QUIT
from player import Player
from tube import Tube
from random import randint
import numpy as np
import sounddevice as sd

class Game:
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    fs = 16000
    block = 256
    mic_level = 0.0 

    y_vel = 0.0
    gravity = 0.6
    THRESH = 0.02
    IMPULSE = -8.0

    def __init__(self):
        self.window = display.set_mode((self.WIDTH,self.HEIGHT))
        self.clock = time.Clock()
        display.set_caption("Flappy Bird")
        
        self.running = True
        self.lose = False
        self.wait = 40

        self.player = Player(50,50,50,50)
        self.tubes = []

        self.generate_tubes(50)

    def audio_cb(self, in_data, frames, time, status):
        if status:
            return
        rms = float(np.sqrt(np.mean(in_data ** 2)))
        self.mic_level = 0.85 * self.mic_level + 0.15 * rms

    def generate_tubes(self,count=10):
        x = self.WIDTH + 700
        for i in range(count):
            y = randint(-300,-50)
            top_tube = Tube(x,y,100,400,'green')
            bottom_tube = Tube(x, top_tube.y+400+200,100,700,'green')
            self.tubes.extend([top_tube, bottom_tube])
            x += 700

    def run(self):
        with sd.InputStream(samplerate = self.fs, channels = 1, blocksize= self.block, callback = self.audio_cb):

            while self.running:
                for e in event.get():
                    if e.type == QUIT:
                        self.running = False

                #self.player.move()
                
                if self.mic_level > self.THRESH:
                    self.y_vel += self.IMPULSE
                self.y_vel += self.gravity
                self.player.rect.y +=int(self.y_vel)


                if self.player.rect.bottom > self.HEIGHT:
                    self.player.rect.bottom = self.HEIGHT
                    self.y_vel = 0 

                if self.player.rect.top < 0:
                    self.player.rect.top = 0
                    self.y_vel = 0   

                if self.lose and self.wait > 1:
                    for t in self.tubes:
                        t.rect.x += 8
                    self.wait -= 1
                else:
                    self.lose = False
                    self.wait = 40
                
                for t in self.tubes:
                    t.move()
                    if self.player.collide(t):
                        self.lose = True

                
                
                self.window.fill("skyblue")
                self.player.draw(self.window)

                for t in self.tubes:
                    t.draw(self.window)
                    
                display.flip()
                self.clock.tick(self.FPS)