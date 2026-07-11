from pygame import event, key, display, Clock, QUIT
from player import Player
from tube import Tube

class Game:
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    def __init__(self):
        self.window = display.set_mode((self.WIDTH,self.HEIGHT))
        self.clock = Clock()
        display.set_caption("Flappy Bird")
        
        self.running = True
        self.lose = False

        self.player = Player(50,50,50,50)
        self.tubes = []

        self.generate_tubes(50)

    def generate_tubes(self,count=10):
        x = self.WIDTH + 700
        for i in range(count):
            top_tube = Tube(x,-200,100,400,'green')
            bottom_tube = Tube(x, top_tube.y+400+200,100,700,'green')
            self.tubes.extend([top_tube, bottom_tube])
            x += 700

    def run(self):
        while self.running:
            for e in event.get():
                if e.type == QUIT:
                    self.running = False

            self.player.move()
            
            for t in self.tubes:
                t.move()
            
            self.window.fill("skyblue")
            self.player.draw(self.window)

            for t in self.tubes:
                t.draw(self.window)
                
            display.flip()
            self.clock.tick(self.FPS)