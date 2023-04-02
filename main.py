from model.snake_model import SnakeModel
from view.snake_gui import GUI
from view.snake_cli import CLI
from controller.snake_controller import SnakeController

WIDTH = 20
HEIGHT = 20

SNAKE_SPEED = 15

def main():
    model = SnakeModel(WIDTH, HEIGHT)
    view = GUI(WIDTH, HEIGHT, SNAKE_SPEED)
    snake = SnakeController(model, view, WIDTH, HEIGHT)

    snake.play()


if __name__ == "__main__": main()  