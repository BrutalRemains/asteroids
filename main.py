import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot     

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    run = True
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):    
                    asteroid.split()
                    shot.kill()


        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()

