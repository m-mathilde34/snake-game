import pygame

class Snake():
    """Stores all to do with the snake."""

    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.screen_rect = snake_game.screen.get_rect()

        self.snake = [(100, 440), (100, 450), (100, 460), (100, 470)]

        #Set skin colour
        self.skin = pygame.Surface((10,10))
        self.skin.fill((152, 133, 88))
        #Set head colour
        self.snake_head = pygame.Surface((10,10))
        self.snake_head.fill((92, 64, 51))

        #Set direction
        self.direction = "UP"

        #Set speed
        self.speed = 10

        #Set is_colliding
        self.is_colliding = False

    def move(self):
        """Move the snake in a given direction.
        Add a new head cell and pop off the tail. This will give the impression of movement in a given direction."""
        if(self.direction == "RIGHT"):
            self.snake.insert(0, (self.snake[0][0] + 10, self.snake[0][1]))
        elif(self.direction == "LEFT"):
            self.snake.insert(0, (self.snake[0][0] - 10, self.snake[0][1]))
        elif(self.direction == "UP"):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 10))
        elif(self.direction == "DOWN"):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 10))
        self.snake.pop()

    def check_wall_collision(self):
        """Method to check whether snake is colliding with wall.
        If snake collides with wall, keep snake at same place.
        Terminate game with a 'GAME OVER' screen.
        Offer player to play again."""
        if(self.snake[0][0] >= 510):
            self.is_colliding = True
        elif(self.snake[0][0] < 10):
            self.is_colliding = True
        elif(self.snake[0][1] >= 560):
            self.is_colliding = True
        elif(self.snake[0][1] < 60):
            self.is_colliding = True
        else:
            self.is_colliding = False

