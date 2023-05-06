import pygame
pygame.init()
widht = 300
height = 300
white = [255,255,255]
black = [0,0,0]
purple = [139,0,255]
red = [255,0,0]
green = [124,227,114]
pink = [244,52,221]
fps = 30
x = 100
y = 130
clock = pygame.time.Clock()
screen = pygame.display.set_mode((widht,height))
pygame.display.set_caption("Крестики-нолики")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(purple)
    pygame.draw.circle(screen,pink,[x,y],15,15)
    x += 5
    y += 5

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()