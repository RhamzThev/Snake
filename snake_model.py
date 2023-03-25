import random

WIDTH = 720
HEIGHT = 480

BLOCK_SIZE = 10
SNAKE_SPEED = 15

class SnakeModel():
    def __init__(self) -> None:
        # DISPLAY DIMENSIONS

        self.score = 0

        self.snake_x = WIDTH / 2
        self.snake_y = HEIGHT / 2

        self.snake = [(self.snake_x, self.snake_y)]
        self.snake_length = 1

        self.snake_direction = "DEFAULT"

        self.fruit_x = random.randrange(1, WIDTH / 10 ) * 10
        self.fruit_y = random.randrange(1, HEIGHT / 10 ) * 10

    def get_score(self):
        return self.score

    def respawn_fruit(self):
        self.fruit_x = random.randrange(1, WIDTH / 10 ) * 10
        self.fruit_y = random.randrange(1, HEIGHT / 10 ) * 10

    def update_model(self, event: str):

        # CHANGE DIRECTION
        if event == "UP" and self.snake_direction != "DOWN":
            self.snake_direction = "UP"
        elif event == "RIGHT" and self.snake_direction != "LEFT":
            self.snake_direction = "RIGHT"
        elif event == "DOWN" and self.snake_direction != "UP":
            self.snake_direction = "DOWN"
        elif event == "LEFT" and self.snake_direction != "RIGHT":
            self.snake_direction = "LEFT"

        # MOVE SNAKE
        if self.snake_direction == "UP":
            self.snake_y -= BLOCK_SIZE
        elif self.snake_direction == "RIGHT":
            self.snake_x += BLOCK_SIZE
        elif self.snake_direction == "DOWN":
            self.snake_y += BLOCK_SIZE
        elif self.snake_direction == "LEFT":
            self.snake_x -= BLOCK_SIZE

        # INSERT POSITION TO SNAKE
        self.snake.insert(0, (self.snake_x, self.snake_y))

        # FRUIT LOGIC
        if (self.snake_x == self.fruit_x) and (self.snake_y == self.fruit_y):
            self.score += 10
            self.respawn_fruit()
        else:
            self.snake.pop()