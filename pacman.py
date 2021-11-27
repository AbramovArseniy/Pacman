import time
import pygame


class Pacman(pygame.sprite.Sprite):
    direction: int  # направление 0 - стоит, 1 - влево, 2 - вправо, 3 - вверх, 4 - вниз
    ind_image: str

    def __init__(self, x, y, screen=None, direction=1):
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
        self.health = 3

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

    def check_collide(self, rect, objects):
        for obj in objects:
            if pygame.sprite.collide_rect(rect, obj.rect):
                if obj.__class__ == "Ghost":
                    self.direction = 0
                    self.health -= 1
                    if self.health == 0:
                        self.death_animation()
                elif obj.__class__ == "Seed":
                    self.score += obj.points
                elif obj.__class__ == "Wall":
                    return 0
        return 1

    def change_image(self, name_image):
        self.image = pygame.image.load(f"sprites/pacman_{name_image}.png")
        self.image = pygame.transform.scale(self.image, (25, 25))

    def change_direction(self, key, objects):
        if key == pygame.K_a:
            if self.check_collide((self.rect.x - 1, self.rect.y), objects):
                self.direction = 1
        elif key == pygame.K_d:
            if self.check_collide((self.rect.x + 1, self.rect.y), objects):
                self.direction = 2
        elif key == pygame.K_w:
            if self.check_collide((self.rect.x, self.rect.y - 1), objects):
                self.direction = 3
        elif key == pygame.K_s:
            if self.check_collide((self.rect.x, self.rect.y + 1), objects):
                self.direction = 4
