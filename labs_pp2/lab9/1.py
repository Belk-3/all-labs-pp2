# Импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройки экрана и частоты кадров
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Игровые переменные
SPEED = 5           # начальная скорость врагов и монет
SCORE = 0           # счёт очков (за проезжающих врагов)
COINS = 0           # количество собранных монет
LEVEL = 1           # текущий уровень

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон
background = pygame.image.load("AnimatedStreet.png")

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])  # 1=бронза, 2=серебро, 3=золото

        # Настройка цвета и радиуса в зависимости от веса
        if self.weight == 1:
            self.radius = 7
            self.color = (255, 165, 0)  # оранжевый
        elif self.weight == 2:
            self.radius = 10
            self.color = (192, 192, 192)  # серый
        else:
            self.radius = 15
            self.color = (255, 255, 0)  # жёлтый

        # Создание изображения круга
        self.image = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # удаляем монету, если она ушла за экран

# Создание игровых объектов
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Таймеры
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

NEW_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_COIN, 2000)  # новая монета каждые 2 сек

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2  # увеличение общей скорости по времени
        if event.type == NEW_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отображение фона
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счёта, монет и уровня
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    level_text = font_small.render(f"Level: {LEVEL}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH//2 - 30, 10))

    # Перемещение и отрисовка всех объектов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка на столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Обработка сбора монет
    collected = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected:
        COINS += coin.weight

        # Увеличиваем уровень за каждые 5 монет
        if COINS % 5 == 0:
            LEVEL += 1
            SPEED += 1  # увеличиваем скорость при переходе на новый уровень

    pygame.display.update()
    FramePerSec.tick(FPS)
