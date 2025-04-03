import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0

    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return

        screen.fill("black")
        player_x = int(SCREEN_WIDTH/2)
        player_y = SCREEN_HEIGHT/2
        player = Player(player_x, player_y)
        player.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
