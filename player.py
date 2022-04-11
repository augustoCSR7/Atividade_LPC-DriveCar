import pygame


class Player:
    def __init__(self):
        self.image_straight = pygame.image.load('sprites/player_car.png').convert_alpha()
        self.image_left = pygame.image.load('sprites/player_car_left.png').convert_alpha()
        self.image_right = pygame.image.load('sprites/player_car_right.png').convert_alpha()
        self.sound_revup = pygame.mixer.Sound('sounds/ogg/car_revving.ogg')
        self.sound_revup.set_volume(0.5)
        self.sound_horn = pygame.mixer.Sound('sounds/ogg/car_horn.ogg')
        self.sound_horn.set_volume(0.3)
        self.image = self.image_straight
        self.trace = (0, 0, 0, 0)
        self.posx, self.posy, self.speed, self.carspeed = 315, 550, 0, -5
        self.moving_left, self.moving_right, self.gas, self.brake = False, False, False, False

    def move(self, game, bg, flag):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameover = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_UP:
                    self.gas = True
                elif event.key == pygame.K_DOWN:
                    self.brake = True
            if event.type == pygame.KEYUP:
                self.moving_left, self.moving_right, self.gas, self.brake = False, False, False, False
                self.sound_revup.stop()
        self.image = self.image_straight
        if self.moving_left and not self.posx - 2.5 <= 205:
            self.posx -= 2.5
            self.image = self.image_left
        if self.moving_right and not self.posx + 2.5 >= 440:
            self.posx += 2.5
            self.image = self.image_right
        if self.gas and self.speed < 300:
            self.speed += 1/3
            bg.speed += .05/3
            flag.speed += .005/3
            self.carspeed += .03/3
            if not pygame.mixer.get_busy():
                self.sound_revup.play(loops=0, maxtime=0, fade_ms=1)
        if self.brake and self.speed > 0:
            self.speed -= 1*2
            bg.speed -= .05/2
            flag.speed -= .005*2
            self.carspeed -= .03*2
            self.sound_revup.stop()
        if self.speed <= 0 or bg.speed <= 0:
            self.speed = 0
            bg.speed = 0

    def draw(self, screen):
        self.trace = screen.blit(self.image, (int(self.posx), int(self.posy)))
        self.trace = (self.trace[0]+5, self.trace[1]+5, self.trace[2]-10, self.trace[3]-10)
        # pygame.draw.rect(screen, (255, 206, 28), self.trace, 2)
