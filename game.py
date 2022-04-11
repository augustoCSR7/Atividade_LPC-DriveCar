'''import pygame.music'''
from turtle import width
import pygame
pygame.init()
from config import Config
from flag import Flag
from background import Background
from car import Car
from player import Player

screen = pygame.display.set_mode((Config.width, Config.height))


pygame.display.set_caption("Drive car")

bg = Background()
player = Player()
car1 = Car(posx=205)
car2 = Car(posx=280)
car3 = Car(posx=360)
car4 = Car(posx=435)
flag = Flag()


class Game:
    def __init__(self):
        self.score, self.gameover, self.difficulty = 0, False, 500
        self.FONT = pygame.font.Font('font/Gamer.ttf', 20)
        self.current_screen = "menu"
        pygame.mixer.music.load('sounds/mp3 and wav/musica_fundo.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
        self.image = pygame.image.load('sprites/crash.png').convert_alpha()
        self.sound_crash = pygame.mixer.Sound('sounds/mp3 and wav/collision.wav')
        self.sound_crash.set_volume(0.3)
        self.sound_point = pygame.mixer.Sound('sounds/mp3 and wav/points.wav')
        self.sound_point.set_volume(0.3)

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_screen = "play"
        # Background image
        back_img = pygame.image.load("sprites/Ford.jpg")
        new_back = pygame.transform.scale(back_img, (700, 800))
        screen.blit(new_back, (0, 0))
        # Font and text
        text = pygame.font.Font('./font/Gamer.ttf', 160)
        write_text = text.render("DRIVE CAR", True, Config.Black)
        write_text_rect = write_text.get_rect(center=(Config.width / 2, 150))
        screen.blit(write_text, write_text_rect)
        text2 = pygame.font.Font('./font/Gamer.ttf', 70)
        write_text2 = text2.render("Press SPACE to start", True, Config.White)
        write_text2_rect = write_text.get_rect(center=(Config.width / 2, 550))
        screen.blit(write_text2, write_text2_rect)
        
        pygame.display.update()
    
    def draw_score(self):
        txt_speed = self.FONT.render('Speed:' + str(int(player.speed)) + ' mph', True, (255, 255, 255))
        txt_score = self.FONT.render('Score:' + str(self.score), True, (255, 255, 255))
        screen.blit(txt_speed, (10, 610))
        screen.blit(txt_score, (10, 640))

    def collision(self):
        p = pygame.Rect(player.trace)
        f = pygame.Rect(flag.trace)
        cars = [pygame.Rect(car1.trace), pygame.Rect(car2.trace), pygame.Rect(car3.trace), pygame.Rect(car4.trace)]
        if p.colliderect(f):
            flag.posx = -100
            game.score += 1
            self.sound_point.play(loops=0, maxtime=0, fade_ms=0)
        for car in cars:
            if p.colliderect(car):
                screen.blit(self.image, (int(player.posx - 80), int(player.posy + 10)))
                pygame.mixer.music.stop()
                #player.sound_revup.stop()
                self.sound_crash.play(loops=0, maxtime=0, fade_ms=1)
                text = pygame.font.Font('./font/Gamer.ttf', 120)
                game_over = text.render("GAME OVER", True, Config.White)
                screen.blit(game_over,(150,300))
                pygame.display.update()
                pygame.time.delay(5000)
                Config.GAME = False


    def mainloop(self):

        bg.draw(screen)
        flag.move(game)
        flag.draw(screen)
        player.move(game, bg, flag)
        player.draw(screen)
        car1.move(player, game)
        car1.draw(screen)
        car2.move(player, game)
        car2.draw(screen)
        car3.move(player, game)
        car3.draw(screen)
        car4.move(player, game)
        car4.draw(screen)
        game.draw_score()
        game.collision()
        pygame.display.update()

    def change_screen(self): 
        if self.current_screen == "play":
            game.mainloop()
        elif self.current_screen == "menu":
            self.menu()

game = Game()
