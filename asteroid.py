import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
#import pygame

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        def __build_asteroids():
            return Asteroid(
                                self.position.x,
                                self.position.y,
                                self.radius - ASTEROID_MIN_RADIUS)
        a1, a2 = __build_asteroids(), __build_asteroids()
        a1_v, a2_v = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        a1.velocity = a1_v * 1.2
        a2.velocity = a2_v * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

