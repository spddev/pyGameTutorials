# Шаблон для создания проектов в Pygame
import pygame
import random


WIDTH = 480 # ширина окна с игрой
HEIGHT = 600 # высота окна с игрой
FPS = 60 # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# инициализация pygame и создание окна
pygame.init()
pygame.mixer.init() # для проигрывания звуков в игре
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0




# Игровой цикл
running = True
while running:
    # Обработка событий (ввода данных)
    for event in pygame.event.get():
        # проверка на закрытие окна
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    clock.tick(FPS)
    # Рэндер/отрисовка
    screen.fill(BLACK)
    # *после* отрисовки чего-либо на экране, переворачиваем наш дисплей
    pygame.display.flip()


pygame.quit()