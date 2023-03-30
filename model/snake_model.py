import random
class SnakeModel():
    def __init__(self, width, height) -> None:
        # DISPLAY DIMENSIONS

        self.__score = 0

        self.__width = width
        self.__height = height

        self.__snake_x = width // 2
        self.__snake_y = height // 2

        self.__snake = [(self.__snake_x, self.__snake_y)]

        self.__snake_direction = "DEFAULT"

        self.__fruit_x = random.randrange(0, width)
        self.__fruit_y = random.randrange(0, height)

    # GETTERS
    def get_score(self):
        return self.__score

    def get_snake(self):
        return self.__snake

    def get_snake_coordinates(self):
        return (self.__snake_x, self.__snake_y)

    def get_fruit_coordinates(self):
        return (self.__fruit_x, self.__fruit_y)

    def is_game_over(self):
        # OUT OF BOUNDS
        if ((self.__snake_x not in range(0, self.__width)) or
        (self.__snake_y not in range(0, self.__height))): return True

        # RAN INTO ITSELF
        if self.__snake[-1] in self.__snake[0:-1]: return True

        return False

    # private method(s)
    def __respawn_fruit(self):

        x = random.randrange(0, self.__width)
        y = random.randrange(0, self.__height)

        if (x, y) not in self.__snake:
            self.__fruit_x = x
            self.__fruit_y = y
        else:
            self.__respawn_fruit()

    def update_model(self, event: str):

        # CHANGE DIRECTION
        if event == "UP" and self.__snake_direction != "DOWN":
            self.__snake_direction = "UP"
        elif event == "RIGHT" and self.__snake_direction != "LEFT":
            self.__snake_direction = "RIGHT"
        elif event == "DOWN" and self.__snake_direction != "UP":
            self.__snake_direction = "DOWN"
        elif event == "LEFT" and self.__snake_direction != "RIGHT":
            self.__snake_direction = "LEFT"

        # MOVE SNAKE
        if self.__snake_direction == "UP":
            self.__snake_y -= 1
        elif self.__snake_direction == "RIGHT":
            self.__snake_x += 1
        elif self.__snake_direction == "DOWN":
            self.__snake_y += 1
        elif self.__snake_direction == "LEFT":
            self.__snake_x -= 1

        # INSERT POSITION TO SNAKE
        self.__snake.insert(0, (self.__snake_x, self.__snake_y))

        # FRUIT LOGIC
        if (self.__snake_x == self.__fruit_x) and (self.__snake_y == self.__fruit_y):
            self.__score += 10
            self.__respawn_fruit()
        else:
            self.__snake.pop()