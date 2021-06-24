import pygame
import random
from game import square_tile, player_object
import time

pygame.init()
screen = pygame.display.set_mode((800, 1000))
clock = pygame.time.Clock()
bg_grid = square_tile(0, 0, screen.get_width(), 800, (0, 0, 0))
smiley = pygame.image.load("game_img.png")


def random_colour():
    return random.choice([(255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 182, 193)])


def generate_tile_list():
    colour_list = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 182, 193)]

    tile_list = []
    for x in range(0, 800, 200):
        colour_order = [0, 1, 2, 3]
        random.shuffle(colour_order)
        for y in range(0, 800, 200):
            tile_list.append(
                square_tile(x, y, 200, 200, colour_list[colour_order[int(y / 200)]]))
    return tile_list


def display_key(x, y, string, fontsize=100):
    text = pygame.font.Font('freesansbold.ttf', fontsize).render(string, True, (0, 0, 0))
    rect = text.get_rect(center=(x, y))
    pygame.draw.rect(screen, (200, 200, 200), rect)
    screen.blit(text, rect)


game_is_running = True
while game_is_running:

    intro_is_active = True
    game_is_active = True

    # Start screen
    while intro_is_active:
        screen.fill((200, 45, 45))

        # Title text
        title_text = pygame.font.Font('freesansbold.ttf', 100).render("COLOUR VOID", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(screen.get_width() / 2, 200))
        screen.blit(title_text, title_rect)

        # Enter box
        display_key(screen.get_width() / 2, 900, "ENTER", 150)

        # W A S D
        display_key(screen.get_width() / 2, 400, "W")
        display_key(screen.get_width() / 2, 525, "S")
        display_key(screen.get_width() / 2 - 100, 525, "A")
        display_key(screen.get_width() / 2 + 100, 525, "D")

        # Get enter button to next screen
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RETURN]:
            intro_is_active = False

        # Used to close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_is_active = False
                game_is_active = False

        pygame.display.update()

    # Countdown used to set duration of each round
    countdown = 3
    player = player_object(386, 386, 35, 35, smiley)

    while game_is_active:
        # Set up round parameters
        clock.tick(30)
        screen.fill((0, 0, 0))

        tile_list = generate_tile_list()
        land_on_colour = random_colour()
        in_a_round = True

        start_time = time.time()

        while in_a_round:

            # To quit using x on the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_a_round = False
                    game_is_active = False
                    game_is_running = False

            # Draw bottom
            pygame.draw.rect(screen, land_on_colour, ((0, 800), (800, 200)))
            round_text = pygame.font.Font('freesansbold.ttf', 50).render("LAND ON THIS COLOUR", True, (0, 0, 0))
            round_text_rect = round_text.get_rect(center=(screen.get_width() / 2, 900))
            screen.blit(round_text, round_text_rect)

            # Draw each colour tile
            for i in tile_list:
                i.draw(screen)

            # When timer reaches 0, delay + next round
            if time.time() - start_time >= countdown:
                # Progressively gets faster, however not by a constant rate. By a variable rate
                if countdown > 1.3:
                    countdown = countdown * 0.80

                is_safe = False
                for i in tile_list:
                    i.end_round_delete(land_on_colour)
                    # If the player successfully lands on the colour
                    if i.check_inside(player) and not is_safe:
                        is_safe = True

                for i in tile_list:
                    i.draw(screen)
                player.draw(screen)
                pygame.display.update()

                if is_safe:
                    delay_s_time = time.time()
                    delay = True

                    # After if statement to update all the other colours
                    while delay:

                        # To quit using x on the window
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                in_a_round = False
                                game_is_active = False
                                game_is_running = False

                        # Draw the ones supposed to land on
                        if time.time() - delay_s_time > 3:
                            delay = False

                    # Next round
                    break

                else:
                    # Getting input to keep playing or not, y or n
                    while True:

                        # To quit using x on the window
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                in_a_round = False
                                game_is_active = False
                                game_is_running = False

                        # Text to ask if user wants to play again or not
                        pygame.draw.rect(screen, (255, 255, 255), ((0, 800), (800, 200)))
                        round_text = pygame.font.Font('freesansbold.ttf', 50).render("PLAY AGAIN? Y or N", True,
                                                                                     (0, 0, 0))
                        round_text_rect = round_text.get_rect(center=(screen.get_width() / 2, 900))
                        screen.blit(round_text, round_text_rect)

                        pressed_keys = pygame.key.get_pressed()
                        if pressed_keys[pygame.K_y]:
                            in_a_round = False
                            game_is_active = False
                            break
                        elif pressed_keys[pygame.K_n]:
                            in_a_round = False
                            game_is_active = False
                            game_is_running = False
                            break

                        pygame.display.update()

            # Update player
            player.update_movement(bg_grid)
            player.draw(screen)

            pygame.display.update()
