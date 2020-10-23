import pygame
from settings import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, mobGrp, playerGrp):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((BLACK))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 10)
        self.x_vel = 20
        self.mobGrp = mobGrp
        self.playerGrp = playerGrp
        self.health = 100
        self.alreadyColliding = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.x_vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.x_vel

        self.bounds()

        if not self.alreadyColliding:
            self.collisions()

        elif self.alreadyColliding:
            if not pygame.sprite.groupcollide(self.playerGrp, self.mobGrp, False, False):
                self.alreadyColliding = False

    def bounds(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

    def collisions(self):
        if pygame.sprite.groupcollide(self.playerGrp, self.mobGrp, False, False):
            self.health -= Mob().mob_damage
            self.alreadyColliding = True
            
            
        
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super(Mob, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH - 25), -25)
        self.y_vel = random.randint(1, 10)
        self.x_vel = random.randint(-10, 10)
        self.mob_damage = 7
        if self.x_vel == 0:
            self.x_vel = 3
        
    def update(self):
        self.movement()
        self.bounds()
        self.generation()

    def movement(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel

    def bounds(self):
        if self.rect.x <= 0 or self.rect.right >= WIDTH:
            self.x_vel *= -1

    def generation(self):
        if self.rect.bottom >= HEIGHT:
            self.rect.y = 0
