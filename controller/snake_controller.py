from model.snake_model import SnakeModel
from view.snake_gui import UI, GUI

WIDTH = 20
HEIGHT = 20

class SnakeController():
    def __init__(self, model: SnakeModel, view: UI) -> None:
        self.model = model
        self.view = view
    
    def play(self):

        while True:
            event = self.view.get_event()
            
            self.model.update_model(event)
            if self.model.is_game_over(): break

            self.view.draw_screen(self.model.get_snake(), self.model.get_fruit_coordinates(), self.model.get_score())

        while True:
            event = self.view.get_game_over_event()

            if event == "RESTART":
                self.model = SnakeModel(WIDTH, HEIGHT)
                self.play()

            self.view.draw_game_over(self.model.get_score())

def main():
    model = SnakeModel(WIDTH, HEIGHT)
    view = GUI(WIDTH, HEIGHT)
    snake = SnakeController(model, view)

    snake.play()


if __name__ == "__main__": main() 