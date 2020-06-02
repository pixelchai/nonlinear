import pygame
from pygame.locals import *

COL_BACKGROUND = (0, 0, 0)
COL_FOREGROUND = (255, 255, 255)

class Demo:
    def __init__(self):

        self.width = 50
        self.height = self.width
        self.off_x = self.width//2
        self.off_y = self.off_x

        self.lower = self.width * -2
        self.upper = self.width * 2
        self.delta = 0.005

        self.size_mult = 20

        self.screen = pygame.display.set_mode((self.size_mult * self.width,
                                               self.size_mult * self.height))

        self._clock = pygame.time.Clock()
        self._fps = 60.0

        self.tickno = 0

    def run(self):
        dt = 1 / self._fps * 1000
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise SystemExit

            self.draw()
            self.update(dt)

            dt = self._clock.tick(self._fps)

    def update(self, dt):
        print(dt)

    def conv(self, x, y):
        return (self.off_x + x)*self.size_mult, (self.height - (self.off_y + y)) * self.size_mult

    def plot(self, x, y, col=COL_FOREGROUND, size=0.01):
        pygame.draw.rect(self.screen, col, (self.conv(x - size/2, y - size/2), (size*self.size_mult, size*self.size_mult)))

    def _draw_axes(self):
        # parametric plot of both x and y axes

        t = self.lower
        while t < self.upper:
            self.plot(0, t)
            self.plot(t, 0)
            t += self.delta

        # # axes markings
        # t = self.lower
        # while t < self.upper:
        #     self.plot(0, t, size=0.5)
        #     self.plot(t, 0, size=0.5)
        #     t += 1
        self.plot(0, 0, size=0.5)

    def draw(self):
        self.screen.fill(COL_BACKGROUND)

        # axes
        self._draw_axes()


        pygame.display.flip()

if __name__ == '__main__':
    Demo().run()
