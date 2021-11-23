import pygame

size = width, height = (600, 700)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)


class Button():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.in_clr = (254,255,89)
        self.act_clr = (178,255,89)

    def draw(self,  x, y, action = None, screen = pygame.display.set_mode(size, pygame.RESIZABLE)):
        mouse = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height :
            pygame.draw.rect(screen, self.in_clr, (x, y, self.width, self.height), 5)
            if c[0] == 1 and action is not None:
                if action == quit:
                    pygame.quit()
                    quit()
                else:
                    action()
        else:
            pygame.draw.rect(screen, self.act_clr, (x, y, self.width, self.height), 5)

def print_t(text, x, y, fs, color = (255, 255,255), ft = 'Courier Regular'):
    font = pygame.font.SysFont(ft, fs, True)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))