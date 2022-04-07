import pygame
pygame.init()

#Name of the game
pygame.display.set_caption("Drive car")

#Screen size
width, height = 800, 700
screen=pygame.display.set_mode((width,height))

#Background image
back_img = pygame.image.load("./img/Ferrari.jpg")
new_back = pygame.transform.scale(back_img,(1000, 700))
screen.blit(new_back,(-100,0))

#Colours
Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (212, 210, 212)
Orange = (183, 119, 0)
Green = (0, 127, 33)
Blue = (0, 97, 148)
Red = (162, 8, 0)
Yellow = (197, 199, 37)

#Font and text
pygame.font.init()
text = pygame.font.Font('./font/Gamer.ttf', 160)
write_text = text.render("DRIVE CAR", 0,White)
screen.blit(write_text,(140,110))
text2 = pygame.font.Font('./font/Gamer.ttf', 70)
write_text2 = text2.render("Press ENTER to start",0,White)
screen.blit(write_text2,(160,550))
pygame.display.update()