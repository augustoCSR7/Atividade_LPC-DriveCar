import pygame
from config import Config


class Background:
    def __init__(self):
        self.bg = pygame.image.load('sprites/street.jpg').convert_alpha()
        self.posy, self.speed = 0, 0
        self.posy2 = - Config.width

        self.new_bg = pygame.transform.scale(self.bg, (Config.width, Config.height))
        self.new_bg2 = pygame.transform.scale(self.bg, (Config.width, Config.height))

    def draw(self, screen):
        self.posy += self.speed
        self.posy2 += self.speed

        if self.posy >= Config.width:
            self.posy = -Config.width

        if self.posy2 >= Config.width:
            self.posy2 = -Config.width

        screen.blit(self.new_bg, (0, int(self.posy)))
        screen.blit(self.new_bg2, (0, int(self.posy2)))
