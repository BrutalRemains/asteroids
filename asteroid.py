import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        velo1 = self.velocity.rotate(random_angle)
        velo2 = self.velocity.rotate(-random_angle)
        
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        
        asteroid1.velocity = velo1 * 1.2
        asteroid2.velocity = velo2 * 1.2
               