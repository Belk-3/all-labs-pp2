import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    draw_mode = 'line'  # 'line', 'rect', 'circle', 'eraser'
    points = []
    start_pos = None  # для фигур

    running = True
    while running:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Выбор цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_k:
                    mode = 'black'

                # Выбор режима рисования
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_l:
                    draw_mode = 'line'
                elif event.key == pygame.K_r:
                    draw_mode = 'rect'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    start_pos = event.pos
                    if draw_mode == 'line':
                        points.append(start_pos)
                        points = points[-256:]
                elif event.button == 3:  # ПКМ
                    radius = max(1, radius - 1)
                elif event.button == 4:  # Колесо вверх
                    radius = min(200, radius + 1)
                elif event.button == 5:  # Колесо вниз
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                if draw_mode == 'line':
                    pos = event.pos
                    points.append(pos)
                    points = points[-256:]
                elif draw_mode == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

            if event.type == pygame.MOUSEBUTTONUP:
                if draw_mode in ['rect', 'circle'] and start_pos:
                    end_pos = event.pos
                    draw_shape(screen, start_pos, end_pos, radius, draw_mode, mode)
                    start_pos = None

        # Очистка экрана убрана — теперь рисуем "навсегда"
        if draw_mode == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        pygame.display.flip()
        clock.tick(60)

# Функция рисования линий
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (255, 255, 0)
    elif color_mode == 'white':
        color = (255, 255, 255)
    elif color_mode == 'black':
        color = (0, 0, 0)
    else:
        color = (c1, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Рисование прямоугольника или круга
def draw_shape(screen, start, end, radius, shape, color_mode):
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
    }
    color = colors.get(color_mode, (255, 255, 255))

    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                       abs(start[0] - end[0]), abs(start[1] - end[1]))
    
    if shape == 'rect':
        pygame.draw.rect(screen, color, rect, width=radius // 5)
    elif shape == 'circle':
        center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        rad = max(abs(end[0] - start[0]), abs(end[1] - start[1])) // 2
        pygame.draw.circle(screen, color, center, rad, width=radius // 5)

main()
