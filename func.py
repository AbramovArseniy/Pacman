import pygame


def update_screen(pacman, screen):
    pacman.change_direction(screen)
    pacman.draw()
    pygame.display.flip()
    screen.fill("Black")
