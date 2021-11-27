import time
import pygame
from pacman import Pacman
from func import update_screen

size = (600, 700)


def main():
    screen = pygame.display.set_mode(size)
    pacman = Pacman(size[0] / 2 - 75, size[1] / 2 + 100, screen)
    objects = []  # массив объектов
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            game_over = event.type == pygame.QUIT
            if event.type == pygame.KEYDOWN:
                pacman.change_direction(objects, event.key)
        update_screen(pacman, screen)  # лучше будет вместо pacman вписать objects и там уже рисовать все объекты
        if pacman.game_over:
            pacman.death_animation()


if __name__ == "__main__":
    main()
