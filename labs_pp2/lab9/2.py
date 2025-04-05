import pygame
import random
import time
from collections import deque

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Timed Food")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GRAY = (192, 192, 192)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Класс еды с весом, цветом и временем жизни
class Food:
    def __init__(self, snake_body):
        self.weight = random.choice([1, 2, 3])
        if self.weight == 1:
            self.color = ORANGE
            self.radius = 7
            self.lifetime = 7
        elif self.weight == 2:
            self.color = GRAY
            self.radius = 10
            self.lifetime = 5
        else:
            self.color = YELLOW
            self.radius = 13
            self.lifetime = 3

        # Генерация позиции вне змеи
        while True:
            self.position = (
                random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            )
            if self.position not in snake_body:
                break

        self.spawn_time = time.time()

    # Проверка, истекло ли время жизни еды
    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime

    # Отрисовка еды
    def draw(self, surface):
        center = (self.position[0] + CELL_SIZE // 2, self.position[1] + CELL_SIZE // 2)
        pygame.draw.circle(surface, self.color, center, self.radius)

# Инициализация змеи
snake = deque([(100, 100)])
direction = (CELL_SIZE, 0)
length = 1
score = 0

# Еда
foods = []

# Шрифт
font = pygame.font.SysFont('Verdana', 20)

# Игровой цикл
running = True
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Движение змеи
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.appendleft(new_head)

    # Ограничение длины
    if len(snake) > length:
        snake.pop()

    # Проверка на столкновение со стенами
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in list(snake)[1:]
    ):
        running = False

    # Добавление еды с шансом
    if len(foods) < 3 and random.randint(0, 100) < 5:
        foods.append(Food(snake))

    # Проверка на поедание
    for food in foods:
        if new_head == food.position:
            length += food.weight
            score += food.weight
            foods.remove(food)
            break

    # Удаление просроченной еды
    foods = [f for f in foods if not f.is_expired()]

    # Отрисовка змеи
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Отрисовка еды
    for food in foods:
        food.draw(screen)

    # Отображение счёта
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
