import numpy as np
import tkinter as tk


class BezierCurve:
    def __init__(self):
        self.points = []
        self.bezier_matrix = np.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 3, 0, 0],
            [1, 0, 0, 0]
        ])
        self.num_points = 100

    def add_point(self, x, y):
        self.points.append([x, y])

    def clear_points(self):
        self.points = []

    def calculate_points(self):

        if len(self.points) != 4:
            raise ValueError("Exactly 4 points is neeeded")

        t_values = np.linspace(0, 1, self.num_points)

        self.T = np.column_stack([t_values ** 3, t_values ** 2, t_values, np.ones_like(t_values)])
        #
        # self.points_matrix = np.array([
        #     [self.points[0][0], self.points[0][1]],
        #     [self.points[1][0], self.points[1][1]],
        #     [self.points[2][0], self.points[2][1]],
        #     [self.points[3][0], self.points[3][1]]
        # ])

        # multiplying
        result = self.T @ self.bezier_matrix @ self.points

        return result

    def get_control_lines(self):
        lines = []
        for i in range(len(self.points)-1):
            lines.append((self.points[i], self.points[i+1]))
        return lines

