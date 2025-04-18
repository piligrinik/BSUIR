import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class EllipseDrawer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.limit = 0
        self.delta = pow(a, 2) + pow(b, 2) + pow(a, 2)*b

    def plot_step(self, ax, x, y):
        cell_size = 2
        rect1 = plt.Rectangle((x * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect1)
        rect2 = plt.Rectangle(((x*(-1)) * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect2)
        rect3 = plt.Rectangle(((x * (-1)) * cell_size, (y * (-1)) * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect3)
        rect4 = plt.Rectangle((x * cell_size, (y * (-1)) * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect4)

    def draw_ellipse(self):
        def plot(ax, x, y):
            self.plot_step(ax, x, y)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(-20, 20)
            ax.set_ylim(-20, 20)

        global fig, ax
        cell_size = 2
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        xticks = [i for i in range(-20, int(20), 2)]

        ax.set_xticks([i for i in range(-20, int(20), 2)])
        ax.set_xticklabels(range(-10, round(20 // cell_size)))
        ax.set_yticks([i for i in range(-20, int(20), 2)])
        ax.set_yticklabels(range(-10, round(20 // cell_size)))

        for x in range(-20, 20, cell_size):
            for y in range(-20, 20, cell_size):
                rect = plt.Rectangle((x, y), cell_size, cell_size, fill=False, edgecolor='gray')
                ax.add_patch(rect)

        a = self.a
        b = self.b
        y = b
        x = 0
        a2 = pow(a, 2)
        b2 = pow(b, 2)
        # plot(ax, x, y)
        delta = self.delta
        s = 0
        s_a = 0
        while y > self.limit:
            if delta > 0:
                s_a = 2*(delta - b2*x) - 1
                if s_a > 0:
                    y = y - 1
                    delta = delta +a2*(1-2*y)
                    plot(ax, x, y)
                else:
                    x = x + 1
                    y = y - 1
                    delta = delta + b2*(2*x + 1) + a2*(1-2*y)
                    plot(ax, x, y)
            elif delta < 0:
                s = 2*(delta - a2*y) - 1
                if s > 0:
                    x = x + 1
                    y = y - 1
                    delta = delta + b2 * (2 * x + 1) + a2 * (1 - 2 * y)
                    plot(ax, x, y)
                else:
                    x = x + 1
                    delta = delta + b2 * (2 * x + 1)
                    plot(ax, x, y)
            else:
                x = x + 1
                y = y - 1
                delta = delta + b2 * (2 * x + 1) + a2 * (1 - 2 * y)
                plot(ax, x, y)

        plt.show()

    def start_debug(self):
        plt.ion()
        self.draw_ellipse()
        plt.ioff()

if __name__ == "__main__":
    app = EllipseDrawer(10, 5)
    app.draw_ellipse()