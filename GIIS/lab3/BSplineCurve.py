import numpy as np
import tkinter as tk


class BSplineCurve:
    def __init__(self):
        self.points = []
        self.basis_matrix = np.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 0, 3, 0],
            [1, 4, 1, 0]
        ]) / 6
        self.num_points = 50

    def add_point(self, x, y):
        self.points.append([x, y])

    def clear_points(self):
        self.points = []

    def get_extended_points(self):
        if len(self.points) < 4:
            return []
        return self.points + self.points[:3]

    def calculate_segment(self, segment_points):
        t_values = np.linspace(0, 1, self.num_points)

        self.T = np.column_stack([t_values ** 3, t_values ** 2, t_values, np.ones_like(t_values)])
        result = self.T @ self.basis_matrix @ segment_points
        return result

    def calculate_points(self):

        if len(self.points) < 4:
            return []

        extended_points = self.get_extended_points()
        curve_points = []

        for i in range(len(self.points)):
            # 4 точки для текущего сегмента
            segment = extended_points[i:i + 4]
            segment_array = np.array(segment)

            curve_points.append(np.array(self.calculate_segment(segment_array)))

        curve_ps=curve_points[0]

        for i in range(1,len(curve_points)):
            curve_ps = np.vstack((curve_ps, curve_points[i]))

        return curve_ps

    def get_control_lines(self):
        lines = []
        for i in range(len(self.points)-1):
            lines.append((self.points[i], self.points[i+1]))
        return lines

