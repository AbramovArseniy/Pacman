import pygame

from func import update_screen
from pacman import Pacman

size = (600, 700)
clock = pygame.time.Clock()


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    pacman = Pacman(size[0] / 2 - 75, size[1] / 2 + 100, screen)
    objects = [pacman]  # массив объектов
    game_over = False

    pygame.mixer.init()

    pacman.sounds.append(pygame.mixer.Sound("sounds/moving_sounds.mp3"))
    pacman.sounds.append(pygame.mixer.Sound("sounds/death_sound.mp3"))

    while not game_over:
        for event in pygame.event.get():
            game_over = event.type == pygame.QUIT
            if event.type == pygame.KEYDOWN:
                objects[0].change_direction(objects, event.key)
                objects[0].game_over = event.key == pygame.K_k
        objects[0].score.draw()
        update_screen(objects, screen)
        if objects[0].game_over:
            objects[0].death_animation(objects)
        clock.tick()

if __name__ == "__main__":
    main()
