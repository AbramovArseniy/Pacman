from dataclasses import dataclass

import pygame


@dataclass
class Speed:
    x: int
    y: int


class Pacman:
    direction: int  # направление 0 - стоит, 1 - влево, 2 - вправо, 3 - вверх, 4 - вниз

    def __init__(self, x, y, speed: Speed, direction=0):
        self.image = pygame.image.load("pacman.png")
        self.game_over = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = speed
        self.score = 0

    def move(self):
        if self.direction == 1:
            self.rect.x -= 1
        elif self.direction == 2:
            self.rect.x += 1
        elif self.direction == 3:
            self.rect.y -= 1
        elif self.direction == 4:
            self.rect.y += 1

    def check_collide(self, objects):
        for obj in objects:
            if pygame.sprite.collide_rect(self.rect, obj.rect):
                if obj.__class__ == Ghost:
                    self.direction = 0
                    self.game_over = True
                elif obj.__class__ == Seed:
                    self.score += 1
                elif obj.__class__ == Wall:
                    self.direction = 0
