import curses
from snake_ui import UI

class CLI(UI):
    def __init__(self, width, height) -> None:
        self.__stdscr  = curses.initscr()

    def get_event(self) -> str:
        event = self.__stdscr.getch()
        if event == curses.KEY_UP:
            return "UP"
        elif event == curses.KEY_RIGHT:
            return "RIGHT"
        elif event == curses.KEY_DOWN:
            return "DOWN"
        elif event == curses.KEY_LEFT:
            return "LEFT"
        
    def draw_screen(self, snake, fruit, score):
        raise NotImplementedError("Subclass must implement this method")

    def get_game_over_event(self):
        event = self.__stdscr.getch()
        if (event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != -1): return "RESTART"

    def draw_game_over(self, score):
        raise NotImplementedError("Subclass must implement this method")