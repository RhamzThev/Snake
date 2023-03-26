from snake_model import SnakeModel
from snake_view import SnakeView
from snake_model import SNAKE_SPEED, WIDTH, HEIGHT

class SnakeController():
    def __init__(self, model: SnakeModel, view: SnakeView) -> None:
        self.model = model
        self.view = view
    
    def play(self):

        running = True

        while running:
            self.view.fps.tick(SNAKE_SPEED)
            event = self.view.get_event()
            
            self.model.update_model(event)

            self.view.draw_screen(self.model.snake, (self.model.fruit_x, self.model.fruit_y), self.model.score)

def main():
    model = SnakeModel()
    view = SnakeView((WIDTH, HEIGHT))
    snake = SnakeController(model, view)
    snake.play()

if __name__ == "__main__": main()