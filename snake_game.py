import sys
import pygame

import apple
import snake
from settings import Settings
from snake import Snake
from apple import Apple


class SnakeGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Set size of game screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        # Set Score's font and size
        self.score = self.settings.score
        self.score_font = pygame.font.SysFont(self.settings.game_font, self.settings.score_size)

        # Create your snake
        self.snake = self.initialise_snake()

        # Create our first apple
        self.apple = self.initialise_apple()

        # Set clock in order to control the snake's speed
        self.clock = pygame.time.Clock()

        # Set the game state, i.e. : START_SCREEN, PLAY or GAME OVER
        self.game_state = "START_SCREEN"

    def initialise_snake(self):
        """Initialises a snake at its starting position with all starting parameter values."""
        new_snake = snake.Snake(self)
        return new_snake

    def initialise_apple(self):
        """Initialises a new apple at a new random location."""
        new_apple = apple.Apple()
        return new_apple

    def draw_borders(self):
        """Draw the game's borders."""
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.left_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.right_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.bottom_border)
        pygame.draw.rect(self.screen, self.settings.border_rgb, self.settings.top_border)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            if self.game_state == "GAME_OVER":
                self._game_over_screen()
                self._check_events()

            elif self.game_state == "START_SCREEN":
                self._start_screen()
                self._check_events()

            elif self.game_state == "PLAY":
                self.clock.tick(self.snake.speed)
                self.snake.move()
                self.snake.check_wall_collision()
                self.snake.check_ouroboros()
                self._check_collision()
                self._check_eating()
                self._check_events()
                self._update_screen()

    def _game_over_screen(self):
        """Create a game over screen which gives the user the option to play again or quit.
        Also displays user's final score."""

        #Load and add ouroborous image
        image = pygame.image.load("./image/ouroboros.png")
        image_y = self.screen.get_height()/2 - image.get_height()/2
        self.screen.blit(image, (self.screen.get_width() / 2 - image.get_width() / 2,
                                 image_y))
        #Paint on screen one time
        pygame.display.flip()

        #Add text
        self.screen.fill(self.settings.go_background)
        go_font = pygame.font.SysFont(self.settings.game_font, self.settings.go_font_size)
        restart_quit_font = pygame.font.SysFont(self.settings.game_font, self.settings.font_size)
        credit_font = pygame.font.SysFont(self.settings.game_font, self.settings.credits_size)

        go_message = go_font.render('OH NO, YOU DIED!', True, self.settings.title_rgb)
        final_score = restart_quit_font.render(f'Final Score : {self.score}', True, self.settings.font_rgb)
        restart = restart_quit_font.render('Restart ? - Press "R"', True, self.settings.font_rgb)
        quit_game = restart_quit_font.render('Quit ? - Press "Q"', True, self.settings.font_rgb)
        credit = credit_font.render("Ouroborous Image by gustavorezende from pixabay", True, self.settings.font_rgb)

        self.screen.blit(go_message, (self.settings.screen_width / 2 - go_message.get_width() / 2,
                                      go_message.get_height()/2))
        self.screen.blit(final_score, (self.settings.screen_width / 2 - final_score.get_width() / 2,
                                       go_message.get_height() + final_score.get_height()))
        self.screen.blit(restart, (self.settings.screen_width / 2 - restart.get_width() / 2,
                                   self.screen.get_height() - quit_game.get_height()*2 -
                                   restart.get_height() - credit.get_height()))
        self.screen.blit(quit_game, (self.settings.screen_width / 2 - quit_game.get_width() / 2,
                                     self.screen.get_height() - quit_game.get_height()*2 - credit.get_height()))
        self.screen.blit(credit, (10, (self.settings.screen_height - credit.get_height() - 10)))

    def _start_screen(self):
        """Creates a start screen which is displaying upon opening the game."""

        # Load and add snake image
        image = pygame.image.load("image/snake_png.png")
        self.screen.blit(image, (self.screen.get_width()/2 - image.get_width()/2, 60))
        # Paint screen one time
        pygame.display.flip()

        # Add text
        self.screen.fill(self.settings.ss_background)
        title_font = pygame.font.SysFont(self.settings.game_font, self.settings.title_size)
        text_font = pygame.font.SysFont(self.settings.game_font, self.settings.font_size)
        credit_font = pygame.font.SysFont(self.settings.game_font, self.settings.credits_size)

        title = title_font.render("Welcome to Snake", True, self.settings.title_rgb)
        start = text_font.render("Press 'P' to start playing!", True, self.settings.font_rgb)
        credit = credit_font.render("Snake Image by artbejo from openclipart", True, self.settings.font_rgb)

        self.screen.blit(title, (self.settings.screen_width / 2 - title.get_width()/2,
                                 60 + image.get_height()))
        self.screen.blit(start, (self.settings.screen_width/2 - start.get_width()/2,
                                 (self.settings.screen_height / 5)*4))
        self.screen.blit(credit, (10,
                                   (self.settings.screen_height-credit.get_height()-10)))

    def _check_collision(self):
        """Check whether snake collides with a wall or whether it is eating itself.
        If so the game is over; Sets the game state to GAME_OVER"""
        if self.snake.wall_colliding or self.snake.ouroboros:
            self.game_state = "GAME_OVER"

    def _check_eating(self):
        """Check whether the snake is colliding with/eating the food.
        If so:
         - make the snake grow
         - remove the food and place a new apple randomly on the board
         - increment score
         - increment snake's speed"""
        if self.snake.snake[0][0] == self.apple.position[0] and self.snake.snake[0][1] == self.apple.position[1]:
            self.snake.grow()
            self.apple = self.initialise_apple()
            self.score += 1
            self.snake.speed += self.snake.speed_increment

    def _check_events(self):
        """Check for user input (key presses or mouse events).
        When game in PLAY, listen for user's directional input.
        When game starts in START_SCREEN, check whether user wants to play or quit.
        When game ends in GAME OVER, check whether user wants to replay or quit.
        If user wants to play again, resets game_state to PLAY and reset snake position and initial parameters."""
        if self.game_state == "PLAY":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        #print("RIGHT")
                        self.snake.direction = "RIGHT"
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        #print("LEFT")
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        #print("UP")
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        #print("DOWN")
                        self.snake.direction = "DOWN"

        if self.game_state == "GAME_OVER":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game_state = "PLAY"
                        self.snake = self.initialise_snake()
                        self.score = 0
                    elif event.key == pygame.K_q:
                        sys.exit()

        if self.game_state == "START_SCREEN":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.game_state = "PLAY"

    def _update_screen(self):
        """Updates the screen every time it is called, then flip to the new screen"""
        # Sets background
        self.screen.fill(self.settings.screen_rgb)
        # Draw borders
        self.draw_borders()
        # Update score
        score_text = self.score_font.render(f'Score: {self.score}', 0, self.settings.font_rgb)
        score_position = (self.settings.screen_width/2 - score_text.get_width()/2, 10)
        self.screen.blit(score_text, score_position)
        # Draw snake
        for snake_pos in self.snake.snake[1:]:
            self.screen.blit(self.snake.skin, snake_pos)
        self.screen.blit(self.snake.snake_head, self.snake.snake[0])
        # Draw apple
        self.screen.blit(self.apple.apple, self.apple.position)

        # Show the most recently drawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    game = SnakeGame()
    game.run_game()
