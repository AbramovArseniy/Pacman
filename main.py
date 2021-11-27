import time
import pygame
from pacman import Pacman

size = (600, 700)
screen = pygame.display.set_mode(size)


def death_animation(pacman):
    pacman.direction = 0
    pacman.change_image("up1")
    update_screen(pacman)
    time.sleep(0.1)
    pacman.change_image("death_1")
    update_screen(pacman)
    time.sleep(0.1)
    pacman.change_image("death_2")
    update_screen(pacman)
    time.sleep(0.1)
    pacman.change_image("death_3")
    update_screen(pacman)
    time.sleep(0.1)
    pacman.change_image("death_4")
    update_screen(pacman)
    time.sleep(0.1)


def update_screen(pacman):
    pacman.draw()
    pygame.display.flip()
    screen.fill("Black")


def main():
    pacman = Pacman(size[0] / 2 - 75, size[1] / 2 + 100, screen)
    objects = []  # массив объектов
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            game_over = event.type == pygame.QUIT
            if event.type == pygame.KEYDOWN:
                pacman.change_direction(event.key, objects)
        update_screen(pacman)  # лучше будет вместо pacman вписать objects и там уже рисовать все объекты
        if pacman.game_over:
            death_animation(pacman)


if __name__ == "__main__":
    main()
