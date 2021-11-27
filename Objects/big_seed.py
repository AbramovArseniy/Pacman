from seed import Seed


class BigSeed(Seed):
    def __init__(self, x=0, y=0, radius=7, points=50, screen=None, color=(255,255,255)):
        super().__init__(x, y, radius, points, screen, color)

