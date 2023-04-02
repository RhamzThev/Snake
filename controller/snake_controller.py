from model.snake_model import SnakeModel
from view.snake_ui import UI



class SnakeController():
    def __init__(self, model: SnakeModel, view: UI, width: int, height: int) -> None:
        self.model = model
        self.view = view
        self.width = width
        self.height = height

    def play(self):

        while True:
            event = self.view.get_event()
            
            self.model.update_model(event)
            if self.model.is_game_over(): break

            self.view.draw_screen(self.model.get_snake(), self.model.get_fruit_coordinates(), self.model.get_score())

        while True:
            event = self.view.get_game_over_event()

            if event == "RESTART":
                self.model = SnakeModel(self.width, self.height)
                self.play()

            self.view.draw_game_over(self.model.get_score())