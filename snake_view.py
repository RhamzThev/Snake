import pygame
from snake_model import BLOCK_SIZE

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

class SnakeView():
    def __init__(self, board) -> None:
        pygame.init()

        self.display = pygame.display.set_mode(board)
        self.fps = pygame.time.Clock()

        pygame.display.set_caption("Snake")

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

    def test_draw_screen(self):
        self.display.fill(RED)

    def draw_screen(self, snake, fruit):
        self.display.fill(BLACK)

        # (snake_x, snake_y) = snake

        for (snake_x, snake_y) in snake:
            pygame.draw.rect(self.display, GREEN, 
                            pygame.Rect(snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE))
        
        (fruit_x, fruit_y) = fruit

        pygame.draw.rect(self.display, WHITE, 
                         pygame.Rect(fruit_x, fruit_y, BLOCK_SIZE, BLOCK_SIZE))
        
        pygame.display.update()