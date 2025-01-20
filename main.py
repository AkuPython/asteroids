import pygame
from pygame.display import update
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60) / 1000
        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        
    # print("Starting asteroids!")
    # print('Screen width:', SCREEN_WIDTH)
    # print('Screen height:', SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
