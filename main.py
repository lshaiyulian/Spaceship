__author__ = 'dielson'

import pygame, sys
from pygame.locals import *
from spaceship import Spaceship

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

BLACK = (0, 0, 0)

spaceship = Spaceship(windowSurface)

keyleft_pressed = False
keyright_pressed = False

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

    pygame.time.delay(15)