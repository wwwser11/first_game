import pygame
import random
import os

def game(FPS, screen, back_colour, clock, all_sprites):
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
        screen.fill(back_colour)  # back color
        all_sprites.draw(screen)
        # flip screen
        pygame.display.flip()
    # close screen
    pygame.quit()