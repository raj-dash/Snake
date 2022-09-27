import pygame
import sys

from pygame.math import Vector2

# initialising pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60

# window
cell_number = 20
cell_size = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")

# main loop
while True:
    for event in pygame.event.get():
        # condition to close the game by pressing the close button on the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing
    pygame.display.update()
    clock.tick(FPS)
