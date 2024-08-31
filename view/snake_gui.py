import sys
import pygame
from view.snake_ui import UI

import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


BLOCK_SIZE = 30

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

ICON = pygame.image.load(resource_path("./assets/favicon.ico"))


class GUI(UI):
    def __init__(self, width, height, snake_speed) -> None:
        pygame.init()
        pygame.display.set_icon(ICON)

        self.__width = width
        self.__height = height

        self.__snake_speed = snake_speed

        self.display = pygame.display.set_mode(
            (width * BLOCK_SIZE, height * BLOCK_SIZE)
        )
        self.fps = pygame.time.Clock()

        pygame.display.set_caption("Snake")

        font_size = (width * BLOCK_SIZE) // 10

        self.heading_one = pygame.font.SysFont("arial", font_size)
        self.heading_two = pygame.font.SysFont("arial", font_size // 2)

    def __center(self, parent, child):
        return (parent // 2) - (child // 2)

    def __quit_game(self):
        pygame.quit()
        sys.exit()

    def get_event(self) -> str:
        for event in pygame.event.get():
            if event.type == 32787:
                self.__quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "UP"
                elif event.key == pygame.K_RIGHT:
                    return "RIGHT"
                elif event.key == pygame.K_DOWN:
                    return "DOWN"
                elif event.key == pygame.K_LEFT:
                    return "LEFT"

            return "DEFAULT"

    def draw_score(self, score):
        surface = self.heading_one.render(f"Score: {score}", True, WHITE)

        display_width = self.display.get_width()
        surface_width = surface.get_width()

        rect = (
            self.__center(display_width, surface_width),
            (self.__height * BLOCK_SIZE) // 24,
        )

        self.display.blit(surface, rect)

    def draw_screen(self, snake, fruit, score):
        self.fps.tick(self.__snake_speed)
        self.display.fill(BLACK)

        self.draw_score(score)

        for snake_x, snake_y in snake:
            pygame.draw.rect(
                self.display,
                GREEN,
                pygame.Rect(
                    snake_x * BLOCK_SIZE, snake_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                ),
            )

        (fruit_x, fruit_y) = fruit

        pygame.draw.rect(
            self.display,
            RED,
            pygame.Rect(
                fruit_x * BLOCK_SIZE, fruit_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
            ),
        )

        pygame.display.update()

    def get_game_over_event(self):
        for event in pygame.event.get():
            if event.type == 32787:
                self.__quit_game()

            if event.type == pygame.KEYDOWN:
                if (
                    event.key != pygame.K_UP
                    and event.key != pygame.K_RIGHT
                    and event.key != pygame.K_DOWN
                    and event.key != pygame.K_LEFT
                ):
                    return "RESTART"

    def draw_game_over(self, score):
        self.fps.tick(self.__snake_speed)
        self.display.fill(BLACK)

        display_width = self.display.get_width()

        # your final score
        final_score_surface = self.heading_one.render(
            f"Final Score: {score}", True, WHITE
        )

        final_score_width = final_score_surface.get_width()
        final_score_height = final_score_surface.get_height()

        final_score_padding = (self.__height * BLOCK_SIZE) // 3

        final_score_rect = (
            self.__center(display_width, final_score_width),
            final_score_padding,
        )

        self.display.blit(final_score_surface, final_score_rect)

        # press any button
        press_surface = self.heading_two.render(
            "Press any button to restart", True, WHITE
        )

        press_width = press_surface.get_width()

        press_padding = (
            final_score_padding + final_score_height + (final_score_padding // 6)
        )

        press_rect = (self.__center(display_width, press_width), press_padding)

        self.display.blit(press_surface, press_rect)

        pygame.display.update()


class InvalidScreenException(Exception):
    def __init__(self, message):
        super().__init__(message)
