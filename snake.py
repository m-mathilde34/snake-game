import pygame

class Snake():

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

    def move(self):
        if(self.direction == "RIGHT"):
            self.snake.insert(0, (self.snake[0][0] + 10, self.snake[0][1]))
        elif(self.direction == "LEFT"):
            self.snake.insert(0, (self.snake[0][0] - 10, self.snake[0][1]))
        elif(self.direction == "UP"):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 10))
        elif(self.direction == "DOWN"):
            self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 10))
        self.snake.pop()
