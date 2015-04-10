__author__ = 'dielson'

import pygame
import sys
from pygame.locals import * # all keys

from spaceship import Spaceship

keyleft_pressed = False
keyright_pressed = False

BLACK = (0, 0, 0)


def init_game():
    global windowSurface, spaceship
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Hello world!')
    spaceship = Spaceship(windowSurface)


def main():
    global event, keyleft_pressed, keyright_pressed
    init_game()
    while True:
        windowSurface.fill(BLACK)
        spaceship.update_position()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    keyleft_pressed = True
                elif event.key == K_RIGHT:
                    keyright_pressed = True
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    keyleft_pressed = False
                elif event.key == K_RIGHT:
                    keyright_pressed = False

        # Moves the spaceship
        if keyright_pressed:
            if spaceship.x_position < 430:
                spaceship.go_right()
        elif keyleft_pressed:
            if spaceship.x_position > 0:
                spaceship.go_left()

        pygame.time.delay(10)


if __name__ == "__main__":
    main()