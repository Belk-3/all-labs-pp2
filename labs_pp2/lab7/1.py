import pygame
import datetime
pygame.init()

# display settings
screen = pygame.display.set_mode((1080, 810))
pygame.display.set_caption("Mikki Clock`s")
Fps = pygame.time.Clock()
done = False

# load images
circle = pygame.image.load("clock.png")
seconds = pygame.image.load("leftarm.png")
minute = pygame.image.load("rightarm.png")
CENTER = (540, 405)

# sizes of the unrotated images
sec_width, sec_height = seconds.get_size()
min_width, min_height = minute.get_size()

while not done:
    t = datetime.datetime.now()
    sec = t.second
    mon = t.minute

    angle_sec = -sec * 6
    angle_min = -mon * 6

    # rotate
    rotated_sec = pygame.transform.rotate(seconds, angle_sec)
    rotated_min = pygame.transform.rotate(minute, angle_min - 50)

    # get rects of rotated images and set the "pivot point" at the base of the hand
    # adjust the position so that base of the hand is at the center
    sec_rect = rotated_sec.get_rect(center=(CENTER[0], CENTER[1]))
    min_rect = rotated_min.get_rect(center=(CENTER[0], CENTER[1]))

    # clear screen and draw
    screen.fill((255, 255, 255))
    screen.blit(circle, (0, 0))
    screen.blit(rotated_min, min_rect)
    screen.blit(rotated_sec, sec_rect)

    # debug center dot
    pygame.draw.circle(screen, (255, 0, 0), CENTER, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    Fps.tick(60)

pygame.quit()
