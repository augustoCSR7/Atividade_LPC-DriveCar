import pygame
from config import*

quit = True
while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit = False