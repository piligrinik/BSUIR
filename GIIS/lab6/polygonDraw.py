import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np


class PolygonEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Editor")
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack(pady=10)
        self.points = []
        self.polygon = None
        self.fill_color = "red"
        self.debug_mode = False
        self.debug_delay = 100

        # Для хранения состояния пикселей
        self.pixel_map = np.zeros((600, 600, 3), dtype=np.uint8) + 255  # Белый фон

        # Панель управления
        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        tk.Button(self.control_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Basic Scanline", command=self.basic_scanline).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Scanline Fill", command=self.scanline_fill).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Flood Fill", command=self.flood_fill).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Scanline Flood", command=self.scanline_flood_fill).pack(side=tk.LEFT,
                                                                                                    padx=5)

        self.debug_var = tk.IntVar()
        tk.Checkbutton(self.control_frame, text="Debug Mode", variable=self.debug_var).pack(side=tk.LEFT, padx=5)

        tk.Label(self.control_frame, text="Fill Color:").pack(side=tk.LEFT, padx=5)
        self.color_var = tk.StringVar(value="black")
        colors = ["black", "green", "blue", "yellow", "purple"]
        ttk.Combobox(self.control_frame, textvariable=self.color_var, values=colors, width=8).pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.close_polygon)

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="purple")
        self.redraw_polygon()
        self.update_pixel_map(x, y, "purple")

    def close_polygon(self, event=None):
        if len(self.points) >= 3:
            self.redraw_polygon(close=True)
            # Обновляем карту пикселей для границ полигона
            for i in range(len(self.points)):
                p1 = self.points[i]
                p2 = self.points[(i + 1) % len(self.points)]
                self.draw_line_on_pixel_map(p1, p2, "blue")

    def redraw_polygon(self, close=False):
        self.canvas.delete("line")
        for i in range(len(self.points) - 1):
            self.canvas.create_line(self.points[i], self.points[i + 1], fill="blue", tags="line")
        if close and len(self.points) >= 3:
            self.canvas.create_line(self.points[-1], self.points[0], fill="blue", tags="line")

    def clear(self):
        self.canvas.delete("all")
        self.points = []
        self.pixel_map = np.zeros((600, 600, 3), dtype=np.uint8) + 255

    def update_pixel_map(self, x, y, color):
        """Обновляет карту пикселей при рисовании"""
        if 0 <= x < 600 and 0 <= y < 600:
            if color == "black":
                self.pixel_map[y, x] = [255, 0, 0]
            elif color == "green":
                self.pixel_map[y, x] = [0, 255, 0]
            elif color == "blue":
                self.pixel_map[y, x] = [0, 0, 255]
            elif color == "yellow":
                self.pixel_map[y, x] = [255, 255, 0]
            elif color == "purple":
                self.pixel_map[y, x] = [128, 0, 128]
            else:  # white
                self.pixel_map[y, x] = [255, 255, 255]

    def draw_line_on_pixel_map(self, p1, p2, color):
        """Рисует линию на карте пикселей"""
        x1, y1 = p1
        x2, y2 = p2

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.update_pixel_map(x1, y1, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def get_pixel_color(self, x, y):
        """Возвращает цвет пикселя в формате строки"""
        if 0 <= x < 600 and 0 <= y < 600:
            pixel = self.pixel_map[y, x]
            if np.array_equal(pixel, [255, 0, 0]):
                return "black"
            elif np.array_equal(pixel, [0, 255, 0]):
                return "green"
            elif np.array_equal(pixel, [0, 0, 255]):
                return "blue"
            elif np.array_equal(pixel, [255, 255, 0]):
                return "yellow"
            elif np.array_equal(pixel, [128, 0, 128]):
                return "purple"
        return "white"

    def basic_scanline(self):
        """Базовая растровая развертка с упорядоченным списком ребер (без активных ребер)"""
        if len(self.points) < 3:
            return

        self.fill_color = self.color_var.get()
        self.debug_mode = bool(self.debug_var.get())

        min_y = min(p[1] for p in self.points)
        max_y = max(p[1] for p in self.points)

        edges = []
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            if p1[1] != p2[1]:
                if p1[1] < p2[1]:
                    edges.append((p1, p2))
                else:
                    edges.append((p2, p1))

        def fill_step(y):
            nonlocal edges
            intersections = []
            for edge in edges:
                p11, p22 = edge
                if p11[1] <= y < p22[1]:
                    dx = p22[0] - p11[0]
                    dy = p22[1] - p11[1]
                    x = p11[0] + dx * (y - p11[1]) / dy
                    intersections.append(x)

            intersections.sort()


            for j in range(0, len(intersections), 2):
                if j + 1 >= len(intersections):
                    break
                x_start = int(intersections[j])
                x_end = int(intersections[j + 1])
                for x in range(x_start, x_end + 1):
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=self.fill_color, outline="")
                    self.update_pixel_map(x, y, self.fill_color)

                y += 1

                if self.debug_mode:
                    self.canvas.after(self.debug_delay, lambda: fill_step(y))
                else:
                    fill_step(y)

        fill_step(min_y)

    def scanline_fill(self):
        if len(self.points) < 3:
            return

        self.fill_color = self.color_var.get()
        self.debug_mode = bool(self.debug_var.get())

        min_y = min(p[1] for p in self.points)
        max_y = max(p[1] for p in self.points)

        edges = []
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            if p1[1] != p2[1]:
                edges.append((p1, p2))

        edge_table = []
        for edge in edges:
            p1, p2 = edge
            if p1[1] < p2[1]:
                ymin, ymax = p1[1], p2[1]
                x = p1[0]
            else:
                ymin, ymax = p2[1], p1[1]
                x = p2[0]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            inv_m = dx / dy if dy != 0 else 0
            edge_table.append((ymin, ymax, x, inv_m))

        edge_table.sort(key=lambda e: e[0])
        active_edges = []

        def fill_step(y):
            nonlocal active_edges

            while edge_table and edge_table[0][0] == y:
                active_edges.append(edge_table.pop(0))

            active_edges = [e for e in active_edges if e[1] != y]
            active_edges.sort(key=lambda e: e[2])

            for i in range(0, len(active_edges), 2):
                x_start = int(active_edges[i][2])
                x_end = int(active_edges[i + 1][2]) if i + 1 < len(active_edges) else x_start
                for x in range(x_start, x_end + 1):
                    self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=self.fill_color, outline="")
                    self.update_pixel_map(x, y, self.fill_color)

            for i in range(len(active_edges)):
                ymin, ymax, x, inv_m = active_edges[i]
                active_edges[i] = (ymin, ymax, x + inv_m, inv_m)

            y += 1

            if y <= max_y and (active_edges or edge_table):
                if self.debug_mode:
                    self.canvas.after(self.debug_delay, lambda: fill_step(y))
                else:
                    fill_step(y)

        fill_step(min_y)

    def flood_fill(self):
        if len(self.points) < 3:
            return
        self.debug_mode = bool(self.debug_var.get())
        self.fill_color = self.color_var.get()
        center_x = sum(p[0] for p in self.points) // len(self.points)
        center_y = sum(p[1] for p in self.points) // len(self.points)

        target_color = self.get_pixel_color(center_x, center_y)
        if target_color == self.fill_color:
            return

        stack = [(center_x, center_y)]
        visited = set()

        def fill_step():
            if not stack:
                return

            x, y = stack.pop()
            if (x, y) in visited:
                self.canvas.after(1, fill_step)
                return

            visited.add((x, y))

            if 0 <= x < 600 and 0 <= y < 600 and self.get_pixel_color(x, y) == target_color:
                self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=self.fill_color, outline="")
                self.update_pixel_map(x, y, self.fill_color)
                stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

            if self.debug_mode and stack:
                self.canvas.after(self.debug_delay, fill_step)
            elif stack:
                fill_step()

        fill_step()

    def scanline_flood_fill(self):
        if len(self.points) < 3:
            return
        self.debug_mode = bool(self.debug_var.get())
        self.fill_color = self.color_var.get()
        center_x = sum(p[0] for p in self.points) // len(self.points)
        center_y = sum(p[1] for p in self.points) // len(self.points)

        target_color = self.get_pixel_color(center_x, center_y)
        if target_color == self.fill_color:
            return

        stack = [(center_x, center_y)]

        def fill_step():
            if not stack:
                return

            x, y = stack.pop()
            left_x = x

            # Находим крайний левый пиксель
            while left_x >= 0 and self.get_pixel_color(left_x, y) == target_color:
                left_x -= 1
            left_x += 1

            span_above = False
            span_below = False
            current_x = left_x

            while current_x < 600 and self.get_pixel_color(current_x, y) == target_color:
                self.canvas.create_rectangle(current_x, y, current_x + 1, y + 1, fill=self.fill_color, outline="")
                self.update_pixel_map(current_x, y, self.fill_color)

                # Проверяем пиксель выше
                if y > 0:
                    if not span_above and self.get_pixel_color(current_x, y - 1) == target_color:
                        stack.append((current_x, y - 1))
                        span_above = True
                    elif span_above and self.get_pixel_color(current_x, y - 1) != target_color:
                        span_above = False

                # Проверяем пиксель ниже
                if y < 599:
                    if not span_below and self.get_pixel_color(current_x, y + 1) == target_color:
                        stack.append((current_x, y + 1))
                        span_below = True
                    elif span_below and self.get_pixel_color(current_x, y + 1) != target_color:
                        span_below = False

                current_x += 1

            if self.debug_mode and stack:
                self.canvas.after(self.debug_delay, fill_step)
            elif stack:
                fill_step()

        fill_step()


if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonEditor(root)
    root.mainloop()