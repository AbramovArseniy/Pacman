import time
import pygame

size = (600, 700)


class Pacman(pygame.sprite.Sprite):
    direction: int  # направление 0 - стоит, 1 - влево, 2 - вправо, 3 - вверх, 4 - вниз
    ind_image: str

    def __init__(self, x, y, screen=None, direction=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/pacman_left2.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.game_over = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.score = 0
        self.screen = screen
        self.rotate = 0
        self.ind_image = "1"
        self.ind_time = 1

    def move(self):
        if self.direction == 1:
            self.rect.x -= 2
            self.change_image("left" + self.ind_image)
        elif self.direction == 2:
            self.rect.x += 2
            self.change_image("right" + self.ind_image)
        elif self.direction == 3:
            self.rect.y -= 2
            self.change_image("up" + self.ind_image)
        elif self.direction == 4:
            self.rect.y += 2
            self.change_image("down" + self.ind_image)

        if self.ind_time == 15:
            if self.ind_image == "1":
                self.ind_image = "2"
            else:
                self.ind_image = "1"
            self.ind_time = 1

        if self.rect.x <= 0:
            self.rect.x = self.screen.get_width() - 25
        elif self.rect.x + 25 >= self.screen.get_width():
            self.rect.x = 0
        elif self.rect.y <= 0:
            self.rect.y = self.screen.get_height() - 25
        elif self.rect.y + 25 >= self.screen.get_height():
            self.rect.y = 0

        self.ind_time += 1
        time.sleep(0.01)

    def draw(self):
        self.move()
        if self.screen:
            self.screen.blit(self.image, self.rect)

    # def check_collide(self, objects):
    #    for obj in objects:
    #        if pygame.sprite.collide_rect(self.rect, obj.rect):
    #            if obj.__class__ == Ghost:
    #                self.direction = 0
    #                self.game_over = True
    #            elif obj.__class__ == Seed:
    #                self.score += obj.points
    #            elif obj.__class__ == Wall:
    #                self.direction = 0

    def change_image(self, name_image):
        self.image = pygame.image.load(f"sprites/pacman_{name_image}.png")
        self.image = pygame.transform.scale(self.image, (25, 25))


def main():
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pacman = Pacman(size[0] / 2 - 75, size[1] / 2 + 100, screen)
    while not pacman.game_over:
        for event in pygame.event.get():
            pacman.game_over = event.type == pygame.QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pacman.direction = 1
                elif event.key == pygame.K_d:
                    pacman.direction = 2
                elif event.key == pygame.K_w:
                    pacman.direction = 3
                elif event.key == pygame.K_s:
                    pacman.direction = 4
        pacman.draw()
        pygame.display.flip()
        screen.fill("Black")
    if pacman.game_over:
        pacman.change_image("")


if __name__ == "__main__":
    main()
