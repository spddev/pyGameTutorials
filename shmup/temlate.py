# Шаблон для создания проектов в Pygame
import pygame
import random


WIDTH = 360 # ширина окна с игрой
HEIGHT = 480 # высота окна с игрой
FPS = 30 # частота кадров в секунду

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