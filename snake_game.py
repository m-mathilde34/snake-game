import sys
import pygame

import snake
from settings import Settings
from snake import Snake


class SnakeGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set size of game screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        # Set text font, size and text --> Score
        self.score = self.settings.score
        score_font = pygame.font.SysFont(self.settings.score_font, self.settings.score_size)
        self.score_text = score_font.render(f'Score: {self.score}', 0, self.settings.score_rgb)

        # Create your snake
        self.snake = self.initialise_snake()

        # Set clock in order to control the snake's speed
        self.clock = pygame.time.Clock()

        # Set the game state, i.e. : PLAY or GAME OVER
        # This will be used in order to create a game over screen
        self.game_state = "PLAY"

    def initialise_snake(self):
        """Initialises a snake at starting position with all starting parameter values."""
        new_snake = snake.Snake(self)
        return new_snake

    def run_game(self):
        """Start the main loop for game"""
        while True:
            if self.game_state == "GAME_OVER":
                self._game_over_screen()
                self._check_events()

            elif self.game_state == "PLAY":
                self.clock.tick(self.snake.speed)
                self.snake.move()
                self.snake.check_wall_collision()
                self._check_collision()
                self._check_events()
                self._update_screen()

    def _game_over_screen(self):
        self.screen.fill(self.settings.go_background)
        go_font = pygame.font.SysFont(self.settings.go_font, self.settings.go_size)
        restart_quit_font = pygame.font.SysFont(self.settings.go_font, self.settings.restart_quit_size)
        go_message = go_font.render('OH NO, YOU DIED :( !', True, self.settings.go_rgb)
        final_score = restart_quit_font.render(f'Final Score : {self.score}', True, self.settings.go_rgb)
        restart = restart_quit_font.render('Restart ? - Press "R"', True, self.settings.go_rgb)
        quit_game = restart_quit_font.render('Quit ? - Press "Q"', True, self.settings.go_rgb)
        self.screen.blit(go_message, (self.settings.screen_width / 2 - go_message.get_width() / 2,
                                      self.settings.screen_height / 2.5 - go_message.get_height() / 2))
        self.screen.blit(final_score, (self.settings.screen_width / 2 - final_score.get_width() / 2,
                                   self.settings.screen_height / 1.5 + final_score.get_height()))
        self.screen.blit(restart, (self.settings.screen_width / 2 - restart.get_width() / 2,
                                   self.settings.screen_height / 1.9 + restart.get_height()))
        self.screen.blit(quit_game, (self.settings.screen_width / 2 - quit_game.get_width() / 2,
                                     self.settings.screen_height / 2 + quit_game.get_height() / 2))

        pygame.display.update()

    def _check_collision(self):
        """Check whether snake collides with a wall. If so : game is over"""
        if self.snake.is_colliding:
            self.game_state = "GAME_OVER"

    def _check_events(self):
        """Check for user input (key presses or mouse events)"""
        """When game ends in GAME OVER, check whether user wants to replay or quit.
        If user wants to play again, resets game_state to PLAY and reset snake position and initial parameters."""
        if self.game_state == "PLAY":
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

        if self.game_state == "GAME_OVER":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game_state = "PLAY"
                        self.snake = self.initialise_snake()
                    elif event.key == pygame.K_q:
                        sys.exit()

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

    def draw_borders(self):
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.left_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.right_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.bottom_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.top_border)


if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()
