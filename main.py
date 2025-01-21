import sys
import pygame
from pygame.display import update
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
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

    # updatable.add(player)
    # drawable.add(player)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
                    break

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    # print("Starting asteroids!")
    # print('Screen width:', SCREEN_WIDTH)
    # print('Screen height:', SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
