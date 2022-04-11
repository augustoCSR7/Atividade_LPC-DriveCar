import pygame
import random
from config import Config


class Flag:
    def __init__(self):
        self.image = pygame.image.load('sprites/flag.png').convert_alpha()
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed = 210, -999, 0
        self.is_moving = False

    def move(self, game):
        if not self.is_moving:
            self.is_moving = True
            self.posx = random.randint(205, 450)
        else:
            self.posy += self.speed
            if self.posy >= Config.height:
                self.is_moving = False
                self.posy = -50
                game.difficulty -= 100
                if game.difficulty <= 100:
                    game.difficulty = 100

    def draw(self, screen):
        self.trace = screen.blit(self.image, (int(self.posx), int(self.posy)))
        # pygame.draw.rect(screen, (255, 206, 28), self.trace, 2)
