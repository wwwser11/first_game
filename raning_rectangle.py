import pygame
import random

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

# make player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # initializing of internal classes of Sprite
        pygame.sprite.Sprite.__init__(self)
        # make img of sprite now its green square
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        # get_rect() оценивает изображение image и высчитывает прямоугольник, способный окружить его.
        self.rect = self.image.get_rect()
        # bring sprite in middle of our screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    # set update rules
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# turn on pygame
pygame.init()
# music
pygame.mixer.init()
# prog screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
# initializing class instance
all_sprites = pygame.sprite.Group()
player = Player()
# add sprite to group
all_sprites.add(player)


# game cycle
running = True
while running:

    # set cycle speed
    clock.tick(FPS)

    # now we can close screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    # rendering
    screen.fill(WHITE)# back color
    all_sprites.draw(screen)
    # flip screen
    pygame.display.flip()
# close screen
pygame.quit()

