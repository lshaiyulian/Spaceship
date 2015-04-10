__author__ = 'dielson'

import pygame

class Spaceship(object):
    def __init__(self, scene):
        self.scene = scene
        self.x_position = 200
        self.y_position = 320
        self.width = 70
        self.height = 60
        self.speed = 5
        self.image = pygame.image.load('spaceship.png')

    def update_position(self):
        self.scene.blit(self.image, (self.x_position, self.y_position))

    def go_left(self):
        self.x_position = self.x_position - self.speed

    def go_right(self):
        self.x_position = self.x_position + self.speed