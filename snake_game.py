import sys
import pygame

from settings import Settings

class SnakeGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set size of game screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Snake")

    def run_game(self):
        """Start the main loop for game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen on each update
            self.screen.fill(self.settings.screen_rgb)
            #Display score on each update

            # Show the most recently drawn screen.
            pygame.display.flip()

if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()