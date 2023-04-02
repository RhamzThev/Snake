class UI():

    def __init__(self, width, height, snake_speed) -> None:
        pass

    def get_event(self) -> str:
        raise NotImplementedError("Subclass must implement this method")

    def draw_screen(self, snake, fruit, score):
        raise NotImplementedError("Subclass must implement this method")

    def get_game_over_event(self):
        raise NotImplementedError("Subclass must implement this method")

    def draw_game_over(self, score):
        raise NotImplementedError("Subclass must implement this method")