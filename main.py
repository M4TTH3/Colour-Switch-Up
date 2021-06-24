import pygame
import random
from game import square_tile, player_object

pygame.init()
screen = pygame.display.set_mode((800, 1000))

clock = pygame.time.Clock()

bg_grid = square_tile(0, 0, screen.get_width(), 800, (0, 0, 0))





def generate_tile_list():
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    pink = (255, 182, 193)

    tile_list = []
    for x in range(0, 800, 200):
        for y in range(0, 800, 200):
            tile_list.append(
                square_tile(x, y, 200, 200, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))


smiley = pygame.image.load("game_img.png")
player = player_object(383, 383, 35, 35, smiley)

intro_is_active = True
game_is_active = True

# Start screen
while intro_is_active:
    screen.fill((200, 45, 45))

    # Title text
    title_text = pygame.font.Font('freesansbold.ttf', 100).render("COLOUR VOID", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(screen.get_width()/2, 200))
    screen.blit(title_text, title_rect)


    #Enter box
    enter_text = pygame.font.Font('freesansbold.ttf', 100).render("ENTER", True, (0, 0, 0))
    text_rect = enter_text.get_rect(center=(screen.get_width() / 2, 600))
    pygame.draw.rect(screen, (200, 200, 200), text_rect)
    screen.blit(enter_text, text_rect)

    #Get enter button to next screen
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RETURN]:
        intro_is_active = False

    # Used to close program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_is_active = False
            game_is_active = False

    pygame.display.update()

while game_is_active:

    clock.tick(400)

    screen.fill((0, 0, 0))

    for i in tile_list:
        i.draw(screen)

    player.update_movement(bg_grid)
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_active = False

    pygame.display.update()
