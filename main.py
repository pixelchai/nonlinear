import pygame

COL_BACKGROUND = (0, 0, 0)

class Demo:
    def __init__(self):
        self.tickno = 0
        self.width = 20
        self.height = 20
        self.size_mult = 20

        self.screen = pygame.display.set_mode((self.size_mult * self.width,
                                               self.size_mult * self.height))

        self._clock = pygame.time.Clock()
        self._fps = 60.0

    def run(self):
        dt = 1 / self._fps * 1000
        while True:
            self.draw()
            self.update(dt)

            dt = self._clock.tick(self._fps)

    def update(self, dt):
        print(dt)

    def draw(self):
        self.screen.fill(COL_BACKGROUND)
        pygame.display.flip()

if __name__ == '__main__':
    Demo().run()