import curses
from view.snake_ui import UI

class CLI(UI):
    def __init__(self, width, height, snake_speed) -> None:
        self.__screen  = curses.initscr()
        curses.curs_set(0)

        self.__window = curses.newwin(width + 2, height + 2, 1, 1)
        self.__window.keypad(True)
        self.__window.timeout(1000 // snake_speed)

    def get_event(self) -> str:
        event = self.__window.getch()
        if event == curses.KEY_UP:
            return "LEFT"
        elif event == curses.KEY_RIGHT:
            return "DOWN"
        elif event == curses.KEY_DOWN:
            return "RIGHT"
        elif event == curses.KEY_LEFT:
            return "UP"
        
    def draw_screen(self, snake, fruit, score):
        self.__window.clear()
        self.__window.border()

        self.__window.addstr(1, 1, 'Score: ' + str(score))

        for (snake_x, snake_y) in snake:
            self.__window.addch(snake_x + 1, snake_y + 1, curses.ACS_CKBOARD)

        (fruit_x, fruit_y) = fruit

        self.__window.addch(fruit_x + 1, fruit_y + 1, curses.ACS_PI)

        self.__window.refresh()

    def get_game_over_event(self):
        event = self.__window.getch()
        if (event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != curses.KEY_UP and
            event != -1): return "RESTART"

    def draw_game_over(self, score):
        self.__window.clear()

        self.__window.addstr(0, 0, f"Final Score: {score}")
        self.__window.addstr(1, 0, "Press any button to restart")
        
        self.__window.refresh()
        