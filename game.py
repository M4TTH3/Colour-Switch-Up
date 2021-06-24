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
            self.colour = (0, 0, 0)

    def draw(self, screen):
        # Rectangle
        pygame.draw.rect(screen, self.colour, self.rect)
        # Border line
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    # Goes after end_round_delete so colour is either one to stand on or black
    def check_inside(self, player):
        # Checks whether the player object touches the tile, then it's safe
        if self.rect.colliderect(player.rect) and not self.colour == (0, 0, 0):
            return True
        else:
            return False

    def has_completely_inside(self, obj):
        return self.rect.contains(obj.rect)


class player_object(pygame.sprite.Sprite):

    # Will draw the image
    def __init__(self, x, y, w, h, img):
        super().__init__()
        self.img = pygame.transform.scale(img, (w, h))
        self.rect = pygame.Rect((x, y), (w, h))

        # Booleans for movements. Used with borders to ensure it doesn't cross
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update_movement(self, grid):
        pressed_keys = pygame.key.get_pressed()

        # Ensures with the movement, directional side does not pass the corresponding side on grid
        if pressed_keys[pygame.K_a] and grid.rect.collidepoint(self.rect.left, 1):
            self.rect.x -= 2
        if pressed_keys[pygame.K_d] and grid.rect.collidepoint(self.rect.right, 1):
            self.rect.x += 2
        if pressed_keys[pygame.K_w] and grid.rect.collidepoint(1, self.rect.top):
            self.rect.y -= 2
        if pressed_keys[pygame.K_s] and grid.rect.collidepoint(1, self.rect.bottom):
            self.rect.y += 2
