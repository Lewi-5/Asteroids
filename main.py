import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((000,000, 000))
        pygame.display.flip


if __name__ == "__main__":
    main()
