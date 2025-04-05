import pygame
import datetime
pygame.init

    
#                                                    display settings
screen = pygame.display.set_mode((1080,810))
pygame.display.set_caption("Mikki Clock`s")
Fps = pygame.time.Clock()
done = False

#imagine 
circle = pygame.image.load("clock.png")
seconds = pygame.image.load("leftarm.png")
minute = pygame.image.load("rightarm.png")
center = (540,405)

# imagine sizes
sec_width, sec_height = seconds.get_size()
min_width, min_height = minute.get_size()

#                                                   main code domain range xDDD
while not done:
    t = datetime.datetime.now()

    sec = t.second
    mon = t.minute 

    angle_sec = -sec * 6
    angle_min = -mon * 6

    pygame.draw.rect(screen, (0,0,255),pygame.Rect(539,404,10,10))

    screen.blit(minute,center)
    screen.blit(seconds,center )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    Fps.tick(60)
pygame.quit()    
