import pygame

size = (width, height) = 600, 700


class DrawableObject:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.rect = pygame.rect.Rect(0, 0, 0, 0)

    def draw(self):
        pass

    def move(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y

    def move_center(self, x: int, y: int) -> None:
        self.rect.centerx = x
        self.rect.centery = y

    def process_event(self, event: pygame.event.Event) -> None:
        pass

    def process_logic(self) -> None:
        pass

    def process_draw(self) -> None:
        pass


class WallObject(DrawableObject):
    def __init__(self, screen, x, y, map):
        super().__init__(screen)
        self.collider = pygame.rect.Rect((x, y), (25, 25))
        self.map = map
        self.x = x
        self.y = y

    def draw(self):
        i = self.y // 25
        j = self.x // 25
        if i < 24 and j < 24:
            if not ((j == 0 or self.map[j - 1][i] == 'wall') or (j == 23 or self.map[j + 1][i] == 'wall') or (
                    i == 0 or self.map[j][i - 1] == 'wall') or (i == 23 or self.map[j][i + 1] == 'wall')) and \
                    self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\pacman_wall_solo.png')
            elif (j == 0 or self.map[j - 1][i] == 'wall') and j != 23 and self.map[j + 1][
                i] != 'wall' and i != 0 and self.map[j][i - 1] != 'wall' and i != 23 and self.map[j][
                i + 1] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_end_right.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and (
                    j == 23 or self.map[j + 1][i] == 'wall') and i != 0 and self.map[j][
                i - 1] != 'wall' and i != 23 and self.map[j][i + 1] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_end_left.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and j != 23 and self.map[j + 1][i] != 'wall' and (
                    i == 0 or self.map[j][i - 1] == 'wall') and i != 23 and self.map[j][i + 1] != 'wall' and \
                    self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_end_down.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and j != 23 and self.map[j + 1][
                i] != 'wall' and i != 0 and \
                    self.map[j][i - 1] != 'wall' and (i == 23 or self.map[j][i + 1] == 'wall') and self.map[j][
                i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_end_up.png')
            elif (j == 0 or self.map[j - 1][i] == 'wall') and (
                    j == 23 or self.map[j + 1][i] == 'wall') and i != 0 and self.map[j][
                i - 1] != 'wall' and i != 23 and self.map[j][i + 1] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_hor.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and j != 23 and self.map[j + 1][i] != 'wall' and (
                    i == 0 or self.map[j][i - 1] == 'wall') and (j == 23 or self.map[j][i + 1] == 'wall') and \
                    self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_vert.png')
            elif (j == 0 or self.map[j - 1][i] == 'wall') and j != 23 and self.map[j + 1][i] != 'wall' and (
                    i == 0 or self.map[j][i - 1] == 'wall') and i != 23 and self.map[j][i + 1] != 'wall' and \
                    self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_right_down.png')
            elif (j == 0 or self.map[j - 1][i] == 'wall') and not (
                    j == 23 or self.map[j + 1][i] == 'wall') and i != 0 and self.map[j][i - 1] != 'wall' and (
                    i == 23 or self.map[j][i + 1] == 'wall') and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_right_up.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and (
                    j == 23 or self.map[j + 1][i] == 'wall') and i != 0 and self.map[j][i - 1] != 'wall' and (
                    i == 23 or self.map[j][i + 1] == 'wall') and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_left_up.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and (j == 23 or self.map[j + 1][i] == 'wall') and \
                    self.map[j][i - 1] and i != 23 and self.map[j][i + 1] != 'wall' and self.map[j][
                i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_left_down.png')
            elif j != 0 and self.map[j - 1][i] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_left.png')
            elif j != 23 and self.map[j + 1][i] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_right.png')
            elif i != 0 and self.map[j][i - 1] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_up.png')
            elif i != 23 and self.map[j][i + 1] != 'wall' and self.map[j][i] == 'wall':
                wall = pygame.image.load('Sprites\walls\Pacman_wall_down.png')
            else:
                wall = pygame.image.load('Sprites\walls\pacman_wall_black.png')
            wall_rect = wall.get_rect(topleft=(j * 25, i * 25 + 100))
            self.screen.blit(wall, wall_rect)


class WallButton:
    def __init__(self, width=70, height=70):
        self.width = width
        self.height = height
        self.in_clr = (254, 255, 89)
        self.act_clr = (178, 255, 89)

    def draw(self, x, y, map_maker, screen=pygame.display.set_mode(size, pygame.RESIZABLE)):
        mouse = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height and c[0]:
            pygame.draw.rect(screen, self.in_clr, (x, y, self.width, self.height), 5)
            wall = pygame.image.load('Sprites\walls\pacman_wall_solo.png')
            wall_rect = wall.get_rect(topleft=(x + self.width//2 - 25 // 2, y + self.height//2 - 25 // 2))
            screen.blit(wall, wall_rect)
            return 'wall'
        else:
            pygame.draw.rect(screen, self.act_clr, (x, y, self.width, self.height), 5)
            wall = pygame.image.load('Sprites\walls\pacman_wall_solo.png')
            wall_rect = wall.get_rect(topleft=(x + self.width//2 - 25 // 2, y + self.height//2 - 25 // 2))
            screen.blit(wall, wall_rect)
            return map_maker.cur_fig


class SeedButton:
    def __init__(self, width=70, height=70):
        self.width = width
        self.height = height
        self.in_clr = (254, 255, 89)
        self.act_clr = (178, 255, 89)

    def draw(self, x, y, map_maker, action=None, screen=pygame.display.set_mode(size, pygame.RESIZABLE)):
        mouse = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height and c[0]:
            pygame.draw.rect(screen, self.in_clr, (x, y, self.width, self.height), 5)
            pygame.draw.circle(screen, (255, 255, 255), (x + self.width//2, y + self.height//2), 3)
            return 'seed'
        else:
            pygame.draw.rect(screen, self.act_clr, (x, y, self.width, self.height), 5)
            pygame.draw.circle(screen, (255, 255, 255), (x + self.width // 2, y + self.height // 2), 3)
            return map_maker.cur_fig


class BigSeedButton:
    def __init__(self, width=70, height=70):
        self.width = width
        self.height = height
        self.in_clr = (254, 255, 89)
        self.act_clr = (178, 255, 89)

    def draw(self, x, y, map_maker, screen=pygame.display.set_mode(size, pygame.RESIZABLE)):
        mouse = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height and c[0]:
            pygame.draw.rect(screen, self.in_clr, (x, y, self.width, self.height), 5)
            pygame.draw.circle(screen, (255, 255, 255), (x + self.width//2, y + self.height//2), 7)
            return 'big_seed'
        else:
            pygame.draw.rect(screen, self.act_clr, (x, y, self.width, self.height), 5)
            pygame.draw.circle(screen, (255, 255, 255), (x + self.width // 2, y + self.height // 2), 7)
            return map_maker.cur_fig


class SaveButton:
    def __init__(self, width=70, height=70):
        self.width = width
        self.height = height
        self.in_clr = (254, 255, 89)
        self.act_clr = (178, 255, 89)

    def draw(self, x, y, scene, action=None, screen=pygame.display.set_mode(size, pygame.RESIZABLE)):
        mouse = pygame.mouse.get_pos()
        c = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height and c[0]:
            pygame.draw.rect(screen, self.in_clr, (x, y, self.width, self.height), 5)
            scene.mp.replace(scene.mp_mk.map)
            main() #Здесь запускается меню
        else:
            pygame.draw.rect(screen, self.act_clr, (x, y, self.width, self.height), 5)
            font = pygame.font.SysFont('Times New Roman', 40)
            data = 'Save'
            ts = font.render(data, False, self.act_clr)
            screen.blit(ts, (x + 10, y + 10))


class Seed(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, radius=3, points=10, screen=None, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.points = points  # количество очков за семя
        self.screen = screen
        self.color = color
        self.radius = radius
        # коллайдер
        self.collider = pygame.Rect((self.x - self.radius / 2, self.y - self.radius / 2),
                                    (self.x + self.radius / 2, self.y
                                     + radius / 2))
        self.draw()

    # отрисовка
    def draw(self):
        if self.screen:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class BigSeed(Seed):
    def __init__(self, x=0, y=0, radius=7, points=50, screen=None, color=(255,255,255)):
        super().__init__(x, y, radius, points, screen, color)


class Map:
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r') as map_file:
            self.map = list(map_file.readlines())
            for i in range(len(self.map)):
                self.map[i] = self.map[i].split()
        for i in range(24):
            for j in range(i):
                self.map[i][j], self.map[j][i] = self.map[j][i], self.map[i][j]

    def replace(self, new_map):
        with open(self.path, 'w') as map_file:
            for i in range(24):
                for j in range(24):
                    self.map[j][i] = new_map[j][i]
                    print(self.map[j][i], end=' ', file=map_file)
                print('', file=map_file)

    def clear(self):
        with open(self.path, 'w') as map_file:
            for i in range(24):
                for j in range(24):
                    self.map[i][j] = 'none'
                    print('none', end=' ', file=map_file)
                print(file=map_file)

    def draw(self, screen):
        for i in range(24):
            for j in range(24):
                if self.map[j][i] == 'seed':
                    seed = Seed(x=j * 25 + 12, y=i * 25 + 112, screen=screen)
                elif self.map[j][i] == 'big_seed':
                    seed = BigSeed(x=j * 25 + 12, y=i * 25 + 112, screen=screen)
                else:
                    wall = WallObject(screen, j*25, i*25, self.map)
                    wall.draw()


class MapMakerScene:
    def __init__(self, screen):
        self.screen = screen
        self.mp = Map('map.txt')
        self.mp_mk = Map('map_maker.txt')
        self.cur_fig = 'wall'

    def main_loop(self):
        saved = False
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mp_mk.clear()
                    game_over = True
                    self.mp_mk.clear()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event)
                    x = (event.pos[0]) // 25
                    y = (event.pos[1] - 100) // 25
                    if 0 <= x < 24 and 0 <= y < 24:
                        if self.mp_mk.map[x][y] != 'none':
                            self.mp_mk.map[x][y] = 'none'
                        else:
                            self.mp_mk.map[x][y] = self.cur_fig
            w_but = WallButton(60, 60)
            self.cur_fig = w_but.draw(100, 10, self, screen=self.screen)
            s_but = SeedButton(60, 60)
            self.cur_fig = s_but.draw(10, 10, self, screen=self.screen)
            save_but = SaveButton(width=100)
            save_but.draw(500, 10, self, screen=self.screen)
            bs_but = BigSeedButton(60, 60)
            self.cur_fig = bs_but.draw(190, 10, self, screen=self.screen)
            self.mp_mk.replace(self.mp_mk.map)
            self.mp_mk.draw(self.screen)
            pygame.display.flip()
