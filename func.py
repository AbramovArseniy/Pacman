import pygame

from buttonc import Button, print_t

# для игры
from dataclasses import dataclass
from math import sqrt
from random import randint
####

pygame.font.init()
size = width, height = (600, 700)
color = (0, 0, 0)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# экран смерти

def dscreen():
    pygame.init()
    b = Button(90, 60)
    exb2 = Button(90, 60)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            start()
        screen.fill(color)
        print_t("U LOST", 200, 50, 80)
        print_t("press Enter to restart", 140, 120, 40)
        print_t("Menu", 62, 620, 35)
        print_t("Exit", 460, 620, 40)
        b.draw(55, 600, main)
        exb2.draw(450, 600, quit)
        pygame.display.flip()

# главное меню

def main():
    pygame.init()
    button1 = button2 = button3 = Button(200, 100)
    exb = Button(90, 60)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(color)
        button1.draw(200, 200, start)
        button2.draw(200, 350)
        button3.draw(200, 500)
        exb.draw(450, 600, quit)

        print_t("Start game", 215, 235, 43)
        print_t("Map editor", 215, 385, 43)
        print_t("  Settings ", 215, 535, 43)
        print_t("Exit", 465, 620, 40)
        print_t("MENU", 210, 50, 80)
        pygame.display.flip()

# код игры

pygame.font.init()
size = width, height = (600, 700) #800, 600
color = (0, 0, 0)
clock = pygame.time.Clock()

@dataclass
class Speed:
    x: int
    y: int

class Ball:
    def __init__(self, x, y, speed: Speed):
        self.image = pygame.image.load((r'C:\Users\azavi\game\basketball.bmp'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self):

        if self.rect.x + self.rect.width == width or self.rect.x == 0:
            self.speed.x *= -1
        if self.rect.x + self.rect.width <= width or self.rect.x >= 0:
            self.rect.x += self.speed.x

        if self.rect.y + self.rect.height == height or self.rect.y == 0:
            self.speed.y *= -1
        if self.rect.y + self.rect.height <= height or self.rect.y >= 0:
            self.rect.y += self.speed.y

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    def collides_with(self, other: "Ball"):
        distance = sqrt((self.rect.x - other.rect.x) ** 2 + (self.rect.y - other.rect.y) ** 2)
        return distance <= self.rect.width

    def coll_x(self):
        return self.rect.x

    def coll_y(self):
        return self.rect.y



balls = [
    Ball(randint(0, width - 100), randint(0, height - 100), Speed(1, 1))
]
def check_collision(screen: pygame.Surface):
    for ind, ball_1 in enumerate(balls):
        for ball_2 in balls[ind:]:
            if (ball_1 is not ball_2) and ball_1.collides_with(ball_2):
                ball_1.speed, ball_2.speed = ball_2.speed, ball_1.speed
                pygame.draw.rect(screen, 'green', ball_1.rect, 3)
                pygame.draw.rect(screen, 'purple', ball_2.rect, 3)
                pygame.display.flip()
                pygame.time.wait(100)

def start():
    o = 5
    pygame.init()
    game_over = False
    while not game_over:
        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        # process logic
        for ball in balls:
            ball.move()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and o >= 15:
            o -= 3
        if keys[pygame.K_d] and o <= 440:
            o += 3
        screen.fill(color)

        if ball.coll_y() == 0 :
            dscreen()                    # после проигрфша откр. экран смерти

        pygame.draw.rect(screen, (255, 105, 180), (o, 53, 151, 35))
        check_collision(screen)
        for ball in balls:
            ball.draw(screen)
        pygame.display.flip()
        if (o - 50 <= ball.coll_x() and ball.coll_x() <= o + 151) and (ball.coll_y() == 88):
            ball.speed.y *= -1
        pygame.time.wait(4)


