__author__ = 'dielson'

import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

BLACK = (0, 0, 0)

#windowSurface.fill(WHITE)
#pygame.display.update()

spaceship = pygame.image.load('spaceship.png')

spaceship_x = 200
spaceship_y = 320
keyleft_pressed = False
keyright_pressed = False

while True:
    windowSurface.fill(BLACK)
    windowSurface.blit(spaceship, (spaceship_x, spaceship_y))
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

    if keyright_pressed:
        if spaceship_x < 430:
            spaceship_x = spaceship_x + 5
    elif keyleft_pressed:
        if spaceship_x > 0:
            spaceship_x = spaceship_x - 5
    pygame.time.delay(10)