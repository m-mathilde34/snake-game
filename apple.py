import random

import pygame


class Apple:
    """Stores all to do with the randomly spawning apples."""

    def __init__(self):
        # Set apple's random position on the screen
        self.position = (random.randrange(10, 510, 10), random.randrange(60, 560, 10))

        # Create an apple surface and assign it a colour
        self.apple = pygame.Surface((10, 10))
        self.apple.fill((210, 43, 43))