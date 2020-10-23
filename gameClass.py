import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.playing = True
        self.running = True

        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0


        self.score = 0

        self.clock = pygame.time.Clock()
        self.sprites_init()

    def sprites_init(self):
        self.all_sprites = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.playerGrp = pygame.sprite.Group()
        self.player = Player(self.mobs, self.playerGrp)
        self.playerGrp.add(self.player)
        for a in range(4):
            m = Mob()
            self.mobs.add(m)
            self.all_sprites.add(m)

        self.all_sprites.add(self.player)

    def new(self):
        self.run()
    
    def run(self):
        while self.playing:
            self.draw()
            self.events()
            self.update()
    
    def draw(self):
        self.clock.tick(FPS)
        self.win.fill(WHITE)
        self.all_sprites.add(self.player)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                print(self.score)
    
    def update(self):
        self.StartTimer()
        self.all_sprites.draw(self.win)
        self.all_sprites.update()
        pygame.display.update()

    def StartTimer(self):

        if self.milliseconds > 1000:
            self.seconds += 1
            self.milliseconds -= 1000
        if self.seconds > 60:
            self.minutes += 1
            self.seconds -= 60
        
        self.score = self.seconds

        self.milliseconds += self.clock.tick_busy_loop(60)

    def startScreen(self):
        pass
    
    def pauseScreen(self):
        pass

    def gameOverScreen(self):
        pass
