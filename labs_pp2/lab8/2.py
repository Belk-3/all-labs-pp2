import pygame
import sys
import random

# Инициализация pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont("Verdana", 20)

# Змейка и еда
snake = [(5, 5), (4, 5), (3, 5)]  # Начальная позиция змейки
direction = (1, 0)  # Движение вправо
food = None

# Игра
score = 0
level = 1
foods_to_level_up = 4
speed = 10  # FPS

clock = pygame.time.Clock()

# Генерация еды в свободном месте
def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

food = generate_food()

# Отображение счёта и уровня
def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

# Основной цикл игры
running = True
while running:
    screen.fill(WHITE)
    draw_score()

    # Отображение еды
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отображение змейки
    for segment in snake:
        pygame.draw.rect(screen, DARKGREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Управление змейкой
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Новая голова змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка выхода за границы
    if (
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
        new_head in snake  # столкновение с самой собой
    ):
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Добавляем новую голову змейки
    snake.insert(0, new_head)

    # Проверка поедания еды
    if new_head == food:
        score += 1

        # Переход на новый уровень
        if score % foods_to_level_up == 0:
            level += 1
            speed += 2  # увеличение скорости

        food = generate_food()
    else:
        snake.pop()  # удаляем хвост, если еда не съедена

    pygame.display.flip()
    clock.tick(speed)
