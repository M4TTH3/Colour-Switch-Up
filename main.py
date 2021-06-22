import pygame
from game import square_tile
pygame.init()
screen = pygame.display.set_mode((800, 800))


active = True
while active:

    screen.fill((0, 0, 0))
    t1 = square_tile(0, 0, 100, 100, (155, 155, 2))
    t1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    pygame.display.update()