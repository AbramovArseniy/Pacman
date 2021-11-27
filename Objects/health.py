import pygame


class Health:

    def __init__(self, screen, image, x=550, y=30):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def draw(self, health):
        for i in range(health):
            self.screen.blit(self.image, (self.rect.x - (30 * i), self.rect.y))
