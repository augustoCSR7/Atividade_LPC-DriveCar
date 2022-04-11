import pygame
from config import Config
import random


class Car:
    def __init__(self, posx):
        self.image0 = pygame.image.load('sprites/enemy_car1.png').convert_alpha()
        self.image1 = pygame.image.load('sprites/enemy_car2.png').convert_alpha()
        self.image2 = pygame.image.load('sprites/enemy_car3.png').convert_alpha()
        self.image_list = (self.image0, self.image1, self.image2)
        self.image = self.image_list[2]
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed = posx, -500, 0
        self.is_moving = False

    def move(self, player, game):
        if not self.is_moving:
            rnd = random.randint(1, game.difficulty)
            if rnd == 50:
                self.is_moving = True
                self.image = self.image_list[random.randint(0, 2)]
                self.speed = random.randint(0, 3)
                if self.speed == 3 and player.speed > 200:
                    player.sound_horn.play(loops=0, maxtime=0, fade_ms=0)
        else:
            self.posy += player.carspeed + self.speed
            if self.posy >= Config.height or self.posy <= -999:
                self.is_moving = False
                self.posy = -200

    def draw(self, screen):
        self.trace = screen.blit(self.image, (int(self.posx), int(self.posy)))
        self.trace = (self.trace[0] + 5, self.trace[1] + 5, self.trace[2] - 10, self.trace[3] - 10)
        # pygame.draw.rect(screen, (255, 206, 28), self.trace, 2)

