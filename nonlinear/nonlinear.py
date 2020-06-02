import math
import os
import sys

import pygame
from pygame.locals import *
import numpy as np

RENDER_MODE = True
RENDER_TIME = 200

COL_BACKGROUND = (0, 0, 0)
COL_FOREGROUND = (255, 255, 255)
COL_DIM = (100, 100, 100)

class Demo:
    def __init__(self):

        self.width = 10
        self.height = self.width
        self.off_x = self.width//2
        self.off_y = self.off_x

        self.lower = self.width * -0.5
        self.upper = self.width * 0.5
        self.delta = 0.01

        self.size_mult = 60

        self.screen = pygame.display.set_mode((self.size_mult * self.width,
                                               self.size_mult * self.height))

        self._clock = pygame.time.Clock()
        self._fps = 60.0

        self.time = 920 + 120 * self._fps
        self.tickno = 0

        if RENDER_MODE:
            os.makedirs("out", exist_ok=True)

    def run(self):
        dt = 1 / self._fps * 1000
        render_target = math.ceil(self._fps * RENDER_TIME)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise SystemExit

            self.draw()
            self.update(dt)

            if not RENDER_MODE:
                dt = self._clock.tick(self._fps)
            else:
                # save image
                pygame.image.save(self.screen, os.path.join("out", "{:06d}.png".format(self.tickno)))
                print("rendered {:06d}/{:06d}".format(self.tickno, render_target))
                if self.tickno >= render_target:
                    print("rendering done")
                    sys.exit()

            self.tickno += 1

    def update(self, dt):
        self.time += dt

    def conv(self, x, y):
        return (self.off_x + x)*self.size_mult, (self.height - (self.off_y + y)) * self.size_mult

    def plot(self, x, y, col=COL_FOREGROUND, size=0.01):
        pygame.draw.rect(self.screen, col, (self.conv(x - size/2, y + size/2), (size*self.size_mult, size*self.size_mult)))

    def f(self, x, y):
        theta = self.time * 0.0005
        mat = np.array([
            [np.cos(theta) + np.cos(x), -np.sin(theta) + np.cos(y)],
            [np.sin(theta) + np.cos(x), np.cos(theta) + np.cos(y)]
        ])
        res = np.matmul(mat, np.array([
            [x],
            [y],
        ]))
        return res[0][0], res[1][0]

    def _draw_axes(self, grid=True):
        if grid:
            t = self.lower
            while t < self.upper:
                s = self.lower
                while s < self.upper:
                    self.plot(*self.f(s, t), col=COL_DIM)
                    self.plot(*self.f(t, s), col=COL_DIM)
                    s += self.delta
                t += 1

        # parametric plot of both x and y axes
        t = self.lower
        while t < self.upper:
            self.plot(*self.f(0, t))
            self.plot(*self.f(t, 0))
            t += self.delta

    def draw(self):
        self.screen.fill(COL_BACKGROUND)
        self._draw_axes()
        pygame.display.flip()

if __name__ == '__main__':
    Demo().run()
