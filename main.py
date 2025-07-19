import pygame
from constants import *


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill("black")
        pygame.display.flip()

        dt += clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()

