import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    run = True
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("black")
        
        
        player.draw(screen)
        player.update(dt)
        
        pygame.display.flip()
        dt += clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()

