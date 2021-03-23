import pygame
import random
import os


# make player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, ship_img, color, w, h):
        self.w = w
        self.h = h
        # initializing of internal classes of Sprite
        pygame.sprite.Sprite.__init__(self)
        # make img of sprite now its green square
        self.image = ship_img
        # ignore back of player pic
        self.image.set_colorkey(color)
        # get_rect() оценивает изображение image и высчитывает прямоугольник, способный окружить его.
        self.rect = self.image.get_rect()
        # bring sprite in middle of our screen
        self.rect.center = (self.w / 2, self.h / 2)

    # set update rules
    def update(self):
        self.rect.x += 5
        if self.rect.left > self.w:
            self.rect.right = 0