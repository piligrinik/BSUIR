import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class ParabolaDrawer:
    # для параболы вида x^2 = 2py
    def __init__(self, p):
        self.p = p
        self.x = 0
        self.y = 0
        self.limit = 20

    def plot_step(self, ax, x, y):
        cell_size = 1
        rect1 = plt.Rectangle((x * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect1)
        rect4 = plt.Rectangle(((x*(-1)) * cell_size, y * cell_size), cell_size, cell_size, color=(0, 0, 0))
        ax.add_patch(rect4)

    def draw_parabola(self):
        def plot(ax, x, y):
            self.plot_step(ax, x, y)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_xlim(-20, 20)
            ax.set_ylim(-20, 20)

        global fig, ax
        cell_size = 1
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        ax.set_xticks([i for i in range(-20, int(20), cell_size)])
        ax.set_xticklabels(range(-20, round(20 // cell_size)))
        ax.set_yticks([i for i in range(-20, int(20), cell_size)])
        ax.set_yticklabels(range(-20, round(20 // cell_size)))

        for x in range(-20, 20, cell_size):
            for y in range(-20, 20, cell_size):
                rect = plt.Rectangle((x, y), cell_size, cell_size, fill=False, edgecolor='gray')
                ax.add_patch(rect)


        x = self.x
        y = self.y
        p = self.p
        delta = 0
        while y < self.limit:
            delta = x**2 - 2 * p * y
            if delta < 0:
                x += 1
                plot(ax, x, y)
            else:
                y +=1
                plot(ax, x, y)

        plt.show()

    def start_debug(self):
        plt.ion()
        self.draw_parabola()
        plt.ioff()

if __name__ == "__main__":
    app = ParabolaDrawer(2)
    app.start_debug()