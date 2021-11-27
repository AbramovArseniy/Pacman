import time
import pygame
from func import update_screen
from Objects.scores import Scores


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
        self.first_x = x
        self.first_y = y
        self.direction = direction
        self.screen = screen
        self.ind_image = "1"
        self.ind_time = 1
        self.health = 3
        self.queue_direction = 0
        self.sounds = []
        self.score = Scores(self.screen, score=0)

    def move(self, objects):
        if self.direction == 1:
            if self.check_collide((self.rect.x - 2, self.rect.y), objects):
                self.rect.x -= 2
                self.change_image("left" + self.ind_image)
            else:
                self.direction = 0
        elif self.direction == 2:
            if self.check_collide((self.rect.x + 2, self.rect.y), objects):
                self.rect.x += 2
                self.change_image("right" + self.ind_image)
            else:
                self.direction = 0
        elif self.direction == 3:
            if self.check_collide((self.rect.x, self.rect.y - 2), objects):
                self.rect.y -= 2
                self.change_image("up" + self.ind_image)
            else:
                self.direction = 0
        elif self.direction == 4:
            if self.check_collide((self.rect.x, self.rect.y + 2), objects):
                self.rect.y += 2
                self.change_image("down" + self.ind_image)
            else:
                self.direction = 0
        if self.ind_time == 15:
            if self.ind_image == "1":
                self.ind_image = "2"
                self.sounds[0].play()
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

    def draw(self, objects):
        self.move(objects)
        if self.screen:
            self.screen.blit(self.image, self.rect)

    def check_collide(self, rect, objects):
        for ind, obj in enumerate(objects):
            if ind != 0:
                if pygame.sprite.collide_rect(rect, obj.rect):
                    if obj.__class__ == "Ghost":
                        self.direction = 0
                        self.health -= 1
                        self.death_animation()
                        if self.health == 0:
                            self.game_over = True
                    elif obj.__class__ == "Seed":
                        self.score.change_score(obj.points)
                    elif obj.__class__ == "Wall":
                        return 0
        return 1

    def change_image(self, name_image):
        self.image = pygame.image.load(f"sprites/pacman_{name_image}.png")
        self.image = pygame.transform.scale(self.image, (25, 25))

    def change_direction(self, objects, key=None):
        if key == pygame.K_a or self.queue_direction == 1:
            if self.check_collide((self.rect.x - 2, self.rect.y), objects):
                self.direction = 1
            else:
                self.queue_direction = 1
        elif key == pygame.K_d or self.queue_direction == 2:
            if self.check_collide((self.rect.x + 2, self.rect.y), objects):
                self.direction = 2
            else:
                self.queue_direction = 2
        elif key == pygame.K_w or self.queue_direction == 3:
            if self.check_collide((self.rect.x, self.rect.y - 2), objects):
                self.direction = 3
            else:
                self.queue_direction = 3
        elif key == pygame.K_s or self.queue_direction == 4:
            if self.check_collide((self.rect.x, self.rect.y + 2), objects):
                self.direction = 4
            else:
                self.queue_direction = 4

    def death_animation(self, objects):
        self.sounds[1].play()
        self.direction = 0
        self.change_image("up1")
        update_screen(objects, self.screen)
        time.sleep(0.2)
        self.change_image("death_1")
        update_screen(objects, self.screen)
        time.sleep(0.2)
        self.change_image("death_2")
        update_screen(objects, self.screen)
        time.sleep(0.2)
        self.change_image("death_3")
        update_screen(objects, self.screen)
        time.sleep(0.2)
        self.change_image("death_4")
        update_screen(objects, self.screen)
        time.sleep(0.5)
        if self.health != 0:
            self.game_over = False
            self.rect.x = self.first_x
            self.rect.y = self.first_y
            time.sleep(0.2)
            self.direction = 1
