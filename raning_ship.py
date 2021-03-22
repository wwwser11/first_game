import pygame
import random
import os
from Player import *
from game_cycle import *

# указал местоположение картинок
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

# size
WIDTH = 780
HEIGHT = 680
FPS = 30

# color (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set back color
back_colour = BLACK

# turn on pygame
pygame.init()
# music
pygame.mixer.init()
# prog screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
# initializing class instance
ship_img = pygame.image.load(os.path.join(img_folder, 'Alien-Frigate.png')).convert()
player = Player(ship_img, back_colour, WIDTH, HEIGHT)
all_sprites = pygame.sprite.Group()
# add sprite to group
all_sprites.add(player)

# game cycle
game(FPS, screen, back_colour, clock, all_sprites)

