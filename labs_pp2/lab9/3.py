import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    # Флаги для рисования разных фигур
    shape_to_draw = None
    start_pos = None
    end_pos = None

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_s:  # Press 's' to draw square
                    shape_to_draw = 'square'
                elif event.key == pygame.K_t:  # Press 't' to draw right triangle
                    shape_to_draw = 'right_triangle'
                elif event.key == pygame.K_e:  # Press 'e' to draw equilateral triangle
                    shape_to_draw = 'equilateral_triangle'
                elif event.key == pygame.K_h:  # Press 'h' to draw rhombus
                    shape_to_draw = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

            # Capture start position for shape drawing
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

            # Capture end position for shape drawing
            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos

        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        # Draw the selected shape
        if shape_to_draw == 'square' and start_pos and end_pos:
            draw_square(screen, start_pos, end_pos)
        elif shape_to_draw == 'right_triangle' and start_pos and end_pos:
            draw_right_triangle(screen, start_pos, end_pos)
        elif shape_to_draw == 'equilateral_triangle' and start_pos and end_pos:
            draw_equilateral_triangle(screen, start_pos, end_pos)
        elif shape_to_draw == 'rhombus' and start_pos and end_pos:
            draw_rhombus(screen, start_pos, end_pos)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Функция для рисования квадрата
def draw_square(surface, start, end):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))  # Размер стороны квадрата
    pygame.draw.rect(surface, (255, 255, 0), (start[0], start[1], side, side))  # Жёлтый квадрат

# Функция для рисования прямоугольного треугольника
def draw_right_triangle(surface, start, end):
    points = [
        start,
        (end[0], start[1]),  # Верхний правый угол
        (start[0], end[1])   # Нижний левый угол
    ]
    pygame.draw.polygon(surface, (255, 0, 0), points)  # Красный прямоугольный треугольник

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(surface, start, end):
    size = abs(end[0] - start[0])  # Используем горизонтальный размер
    height = (3 ** 0.5 / 2) * size  # Высота для равностороннего треугольника
    points = [
        (start[0], end[1]),  # Левый угол
        (start[0] + size, end[1]),  # Правый угол
        (start[0] + size / 2, end[1] - height)  # Верхний угол
    ]
    pygame.draw.polygon(surface, (0, 255, 0), points)  # Зелёный равносторонний треугольник

# Функция для рисования ромба
def draw_rhombus(surface, start, end):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    points = [
        (start[0] + width // 2, start[1]),  # Верхняя вершина
        (start[0] + width, start[1] + height // 2),  # Правая вершина
        (start[0] + width // 2, start[1] + height),  # Нижняя вершина
        (start[0], start[1] + height // 2)  # Левая вершина
    ]
    pygame.draw.polygon(surface, (255, 0, 255), points)  # Розовый ромб

main()
