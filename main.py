import time
import pygame
from pacman import Pacman
from func import update_screen

size = (600, 700)


def main():
    screen = pygame.display.set_mode(size)
    pacman = Pacman(size[0] / 2 - 75, size[1] / 2 + 100, screen)
    objects = [pacman]  # массив объектов
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            game_over = event.type == pygame.QUIT
            if event.type == pygame.KEYDOWN:
                objects[0].change_direction(objects, event.key)
        update_screen(objects, screen)
        if objects[0].game_over:
            objects[0].death_animation()


if __name__ == "__main__":
    main()
