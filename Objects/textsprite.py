import pygame


class Text_sprite:
    def __init__(self, text, screen, x, y, color=(255, 255, 255), text_size=20):
        self.__text = str(text)
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.color = color
        self.textsurface = self.font.render(self.__text, False, self.color)
        self.x = x
        self.y = y

    def change_text(self, text):
        self.__text = str(text)
        self.textsurface = self.font.render(self.__text, False, self.color)

    def draw(self):
        self.screen.blit(self.textsurface, (self.x, self.y))
