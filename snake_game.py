import sys
import pygame

from settings import Settings
from snake import Snake

class SnakeGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set size of game screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Snake")

        # Set text font, size and text --> Score
        font = pygame.font.SysFont(self.settings.score_font, self.settings.score_size)
        self.score_text = font.render(f'Score: {self.settings.score}', 0, self.settings.score_rgb)

        # Get snake
        self.snake = Snake(self)

        # Set clock
        self.clock = pygame.time.Clock()

    def draw_borders(self):
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.left_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.right_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.bottom_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.top_border)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            self.clock.tick(self.snake.speed)
            self.snake.move()
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Check for user input (key presses or mouse events)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    print("RIGHT")
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    print("LEFT")
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    print("UP")
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    print("DOWN")
                    self.snake.direction = "DOWN"


    def _update_screen(self):
        """Updates the screen every time it is called, then flip to the new screen"""
        # Redraw the screen on each update
        self.screen.fill(self.settings.screen_rgb)
        # Draw borders
        self.draw_borders()
        # Update score
        self.screen.blit(self.score_text, self.settings.score_position)
        # Draw snake
        for snake_pos in self.snake.snake[1:]:
            self.screen.blit(self.snake.skin, snake_pos)
        self.screen.blit(self.snake.snake_head, self.snake.snake[0])

        # Show the most recently drawn screen.
        pygame.display.flip()



if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()