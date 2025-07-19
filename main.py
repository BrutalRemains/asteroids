import pygame
from constants import *

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((0,0,0))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

