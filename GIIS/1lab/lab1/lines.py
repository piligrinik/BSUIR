import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class LineDrawer:

    def plot_step(self, ax, x, y, cell_size):
        rect = plt.Rectangle((x * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect)

    def plot_step_transperancy(self, ax, x, y, c, cell_size):
        rect = plt.Rectangle((x * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0, c))
        ax.add_patch(rect)

    def dda_line(self, ax, x0, y0, x1, y1, cell_size):
        def plot(x, y):
            self.plot_step(ax, x, y, cell_size)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)

        dx = x1 - x0
        dy = y1 - y0
        step = max(abs(dx), abs(dy))
        if step != 0:
            stepX = dx / step
            stepY = dy / step
            f_stepX = 1 if stepX != 0 else 0
            f_stepy = 1 if stepY != 0 else 0
            x = x0 + 0.5*f_stepX
            y =  y0 + 0.5*f_stepy
            plot(int(x), int(y))
            for i in range(step):
                plot(int(x0 + i*stepX),int(y0 + i*stepY))

    def bresenhams_lineX(self, ax, x0, y0, x1, y1, cell_size):
        def plot(x, y):
            self.plot_step(ax, x, y, cell_size)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        dir = -1 if dy < 0 else 1
        dy *= dir
        if dx != 0:
            y = y0
            p = 2 * dy - dx
            for i in range(dx):
                plot(x0 + i, y)
                if p >= 0:
                    y += dir
                    p = p - 2 * dx
                p = p + 2 * dy

    def bresenhams_lineY(self, ax, x0, y0, x1, y1, cell_size):
        def plot(x, y):
            self.plot_step(ax, x, y, cell_size)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
        if y0 > y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        dir = -1 if dx < 0 else 1
        dx *= dir
        if dy != 0:
            x = x0
            p = 2 * dx - dy
            for i in range(dy):
                plot(x, y0 + i)
                if p >= 0:
                    x += dir
                    p = p - 2 * dy
                p = p + 2 * dx

    def bresenhams_line(self, ax, x0, y0, x1, y1, cell_size):
        if abs(x1-x0) > (y1-y0):
            self.bresenhams_lineX(ax, x0, y0, x1, y1, cell_size)
        else:
            self.bresenhams_lineY(ax, x0, y0, x1, y1, cell_size)


    def wu_line(self, ax, x0, y0, x1, y1, cell_size):
        def plot(x, y, c):
            self.plot_step_transperancy(ax, x, y, c, cell_size)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)

        dx = x1 - x0
        dy = y1 - y0

        if abs(x1 - x0) > abs(y1 - y0):
            if x0 > x1:
                x0, x1 = x1, x0
                y0, y1 = y1, y0

            gradient = dy / dx if dx != 0 else 1
            y = y0 + gradient * (round(x0) - x0)
            # для начальной точки
            ovelap = 1 - (x0 + 0.5 - int(x0 + 0.5))
            xpxl1 = round(x0)
            ypxl1 = int(y)
            plot(xpxl1, ypxl1, 1 - (y - int(y)) * ovelap)
            plot(xpxl1, ypxl1 + 1, (y - int(y)) * ovelap)
            intery = y + gradient
            # для конечной
            x_end = round(x1)
            y = y1 + gradient * (x_end - x1)
            ovelap = (x1 + 0.5 - int(x1 + 0.5))
            xpxl2 = x_end
            ypxl2 = int(y)
            plot(xpxl2, ypxl2, 1 - (y - int(y)) * ovelap)
            plot(xpxl2, ypxl2 + 1, (y - int(y)) * ovelap)

            for x in range(xpxl1 + 1, xpxl2):
                plot(x, int(intery), 1 - (intery - int(intery)))
                plot(x, int(intery) + 1, intery - int(intery))
                intery = intery + gradient

        else:
            if y1 < y0:
                x0, x1 = x1, x0
                y0, y1 = y1, y0
            gradient = dx / dy if dy != 0 else 1
            x = x0 + gradient * (round(y0) - y0)
            # для начальной точки
            ovelap = 1 - (y0 + 0.5 - int(y0 + 0.5))
            ypxl1 = round(y0)
            xpxl1 = int(x)
            plot(xpxl1, ypxl1, 1 - (x - int(x)) * ovelap)
            plot(xpxl1, ypxl1 + 1, (x - int(x)) * ovelap)
            intery = x + gradient
            # для конечной
            y_end = round(y1)
            x = x1 + gradient * (y_end - y1)
            ovelap = (y1 + 0.5 - int(y1 + 0.5))
            ypxl2 = y_end
            xpxl2 = int(x)
            plot(xpxl2, ypxl2, 1 - (x - int(x)) * ovelap)
            plot(xpxl2, ypxl2 + 1, (x - int(x)) * ovelap)

            for y in range(ypxl1 + 1, ypxl2):
                plot(int(intery), y, 1 - (intery - int(intery)))
                plot(int(intery) + 1, y, intery - int(intery))
                intery = intery + gradient

    def draw_line(self, method,  x0, y0, x1, y1, cell_size):

        global fig, ax
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)

        ax.set_xticks([i for i in range(0, int(100), cell_size)])
        ax.set_xticklabels(range(round(100//cell_size))) if cell_size % 2 == 0 else ax.set_xticklabels(range(round(100//cell_size)+1))
        ax.set_yticks([i for i in range(0, int(100), cell_size)])
        ax.set_yticklabels(range(round(100//cell_size))) if cell_size % 2 == 0 else ax.set_yticklabels(range(round(100//cell_size)+1))

        for x in range(0, 100, cell_size):
            for y in range(0, 100, cell_size):
                rect = plt.Rectangle((x, y), cell_size, cell_size, fill=False, edgecolor='gray')
                ax.add_patch(rect)

        match(method):
            case 1:
                self.dda_line(ax, x0, y0, x1, y1, cell_size)
            case 2:
                self.bresenhams_line(ax, x0, y0, x1, y1, cell_size)
            case 3:
                self.wu_line(ax, x0, y0, x1, y1, cell_size)
            case _:
                self.dda_line(ax, x0, y0, x1, y1, cell_size)

        plt.show()

    def start_debug(self, method,  x0, y0, x1, y1, cell_size):
        plt.ion()
        self.draw_line(method,  x0, y0, x1, y1, cell_size)
        plt.ioff()

            # self.wu_line(ax, x0, y0, x1, y1, cell_size)
        # self.dda_line(ax, x0, y0, x1, y1, cell_size)
        # self.bresenhams_line(ax, x0, y0, x1, y1, cell_size)

        


