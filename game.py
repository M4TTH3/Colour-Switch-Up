import pygame
# Subclassing the Sprite class to build the features


class square_tile(pygame.sprite.Sprite):

    # Used for tile grid and background.
    def __init__(self, x, y, w, h, colour):
        super().__init__()
        # Hit box
        self.rect = pygame.Rect((x, y), (w, h))
        # Colour to draw and compare
        self.colour = colour

    # Checks whether at the end of the round if it was the colour to land on
    def end_round_delete(self, colour):
        # If not right colour, deleted turning black
        if not self.colour == colour:
            self.colour == (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    # Goes after end_round_delete so colour is either one to stand on or black
    def check_inside(self, player_object):
        # Checks whether the player object touches the tile, then it's safe
        if self.rect.contains(player_object) and not self.colour == (0, 0, 0):
            return True
        else:
            return False


class player_object(pygame.sprite.Sprite):

    def __init__(self):
        pass


# class tile(game_object):
# init: colour_str
# colour_str used to determines colour and for booleans

# update_colour(self, colour_str): updates colour

# the draw function will contain if to adjust colour based on string
