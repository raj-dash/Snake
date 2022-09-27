import pygame
import sys
from pygame.math import Vector2

class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False


class Main():
    def __init__(self):
        self.snake = Snake()

    def draw_elements(self):
        self.draw_grass()

    def draw_grass(self):
        global grass_colour
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_colour, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_colour, grass_rect)


# initialising pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60
main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

# window
cell_number = 20
cell_size = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")

# colors
lime = (175, 215, 70)
grass_colour = (167, 209, 61)

# main loop
while True:
    for event in pygame.event.get():
        # condition to close the game by pressing the close button on the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            pass

    # drawing
    screen.fill(lime)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FPS)
