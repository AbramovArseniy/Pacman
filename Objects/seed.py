import pygame


class Seed(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, radius=3, points=10, screen=None, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.points = points   # количество очков за семя
        self.screen = screen
        self.color = color
        self.radius = radius
        # коллайдер
        self.collider = pygame.Rect((self.x - self.radius/2, self.y - self.radius/2), (self.x+self.radius/2, self.y
                                                                                       + radius/2))
        self.draw()

    # отрисовка
    def draw(self):
        if self.screen:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
