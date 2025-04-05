import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Begin xDDD")
fps = pygame.time.Clock()

ball_r = 25
ball_x = 400
ball_y = 300
ball_m =  20

done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 144, 0), (0, 0, 800, 600))  
    pygame.draw.rect(screen, (255,255,255) , (30,20,740,560))

    pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y), ball_r)

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and ball_x+ball_m <= 800-30:
        ball_x += ball_m
    if key[pygame.K_LEFT] and ball_x - ball_m >= 30:                
        ball_x -= ball_m
    if key[pygame.K_UP] and ball_y - ball_m >= 20+15:
        ball_y -= ball_m
    if key[pygame.K_DOWN] and ball_y + ball_m <= 600-20-15:
        ball_y += ball_m
 
    pygame.display.flip()
    fps.tick(20)
