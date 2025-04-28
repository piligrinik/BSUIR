import tkinter as tk
import numpy as np
from math import atan2
from tkinter import messagebox

class PolygonEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Editor")
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack(pady=10)
        self.points = []  # Точки полигона
        self.segment_points = []  # Точки для отрезка
        self.polygon = None
        self.normals = []
        self.hull_graham = []
        self.hull_jarvis = []
        self.intersections = []  # Точки пересечения

        # Панель управления
        self.control_frame = tk.Frame(root)
        self.control_frame.pack()
        tk.Button(self.control_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Check Convex", command=self.check_convex).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Show Normals", command=self.show_normals).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Graham Hull", command=self.graham_hull).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Jarvis Hull", command=self.jarvis_hull).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Draw Segment", command=self.start_segment_mode).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Find Intersections", command=self.find_intersections).pack(side=tk.LEFT, padx=5)

        # Привязка событий
        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.close_polygon)
        self.segment_mode = False  # Режим рисования отрезка

    def start_segment_mode(self):

        self.segment_mode = True
        self.segment_points = []
        self.canvas.delete("segment")
        self.canvas.delete("intersection")
        self.intersections = []
        self.canvas.bind("<Button-1>", self.add_segment_point)

    def add_segment_point(self, event):

        x, y = event.x, event.y
        self.segment_points.append((x, y))
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black", tags="segment")
        if len(self.segment_points) == 2:
            self.canvas.create_line(self.segment_points[0], self.segment_points[1], fill="cyan", tags="segment")
            self.segment_mode = False
            self.canvas.bind("<Button-1>", self.add_point)  # Вернуть стандартный режим
        self.redraw_polygon(close=True)

    def add_point(self, event):
        self.close_polygon()
        if not self.segment_mode:
            x, y = event.x, event.y
            self.points.append((x, y))
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="purple")
            self.redraw_polygon()

    def close_polygon(self, event=None):
        if len(self.points) >= 3:
            self.redraw_polygon(close=True)

    def redraw_polygon(self, close=False):
        self.canvas.delete("line")
        for i in range(len(self.points)-1):
            self.canvas.create_line(self.points[i], self.points[i+1], fill="blue", tags="line")
        if close and len(self.points) >= 3:
            self.canvas.create_line(self.points[-1], self.points[0], fill="blue", tags="line")

    def clear(self):
        self.canvas.delete("all")
        self.points = []
        self.segment_points = []
        self.normals = []
        self.hull_graham = []
        self.hull_jarvis = []
        self.intersections = []
        self.segment_mode = False
        self.canvas.bind("<Button-1>", self.add_point)

    def is_convex_polygon(self, points):
        if len(points) < 3:
            return False
        n = len(points)
        sign = 0
        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            p3 = points[(i + 2) % n]
            cross = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
            if cross != 0:
                if sign == 0:
                    sign = np.sign(cross)
                elif sign != np.sign(cross):
                    return False
        return True

    def check_convex(self):
        if len(self.points) < 3:
            messagebox.showinfo("Error", "Need at least 3 points!")
            return
        is_convex = self.is_convex_polygon(self.points)
        messagebox.showinfo("Convex Check", f"Polygon is {'convex' if is_convex else 'not convex'}")

    def get_inner_normals(self, points):
        n = len(points)
        normals = []
        centroid = np.mean(points, axis=0)
        for i in range(n):
            p1 = np.array(points[i])
            p2 = np.array(points[(i + 1) % n])
            edge = p2 - p1
            normal = np.array([-edge[1], edge[0]])
            mid_point = (p1 + p2) / 2
            to_centroid = centroid - mid_point
            if np.dot(to_centroid, normal) < 0:
                normal = -normal
            normal = normal / np.linalg.norm(normal) * 20
            normals.append((mid_point, normal))
        return normals

    def show_normals(self):
        if len(self.points) < 3:
            messagebox.showinfo("Error", "Need at least 3 points!")
            return
        self.canvas.delete("normal")
        self.normals = self.get_inner_normals(self.points)
        for mid_point, normal in self.normals:
            end_point = mid_point + normal
            self.canvas.create_line(mid_point[0], mid_point[1], end_point[0], end_point[1],
                                  fill="green", arrow=tk.LAST, tags="normal")

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    def graham_hull(self):
        if len(self.points) < 3:
            messagebox.showinfo("Error", "Need at least 3 points!")
            return
        points = sorted(self.points)
        n = len(points)
        stack = []
        for i in range(n):
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], points[i]) != -1:
                stack.pop()
            stack.append(points[i])
        lower = stack[:]
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], points[i]) != -1:
                stack.pop()
            stack.append(points[i])
        stack.pop()
        self.hull_graham = lower + stack
        self.canvas.delete("hull")
        for i in range(len(self.hull_graham)):
            self.canvas.create_line(self.hull_graham[i], self.hull_graham[(i+1)%len(self.hull_graham)],
                                  fill="purple", tags="hull")

    def jarvis_hull(self):
        if len(self.points) < 3:
            messagebox.showinfo("Error", "Need at least 3 points!")
            return
        n = len(self.points)
        hull = []
        l = min(range(n), key=lambda i: (self.points[i][0], self.points[i][1]))
        p = l
        while True:
            hull.append(self.points[p])
            q = (p + 1) % n
            for i in range(n):
                if self.orientation(self.points[p], self.points[i], self.points[q]) == -1:
                    q = i
            p = q
            if p == l:
                break
        self.hull_jarvis = hull
        self.canvas.delete("hull")
        for i in range(len(self.hull_jarvis)):
            self.canvas.create_line(self.hull_jarvis[i], self.hull_jarvis[(i+1)%len(self.hull_jarvis)],
                                  fill="orange", tags="hull")

    def find_intersection(self, p1, p2, q1, q2):
        def on_segment(p, q, r):
            return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                    q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

        o1 = self.orientation(p1, p2, q1)
        o2 = self.orientation(p1, p2, q2)
        o3 = self.orientation(q1, q2, p1)
        o4 = self.orientation(q1, q2, p2)

        # Общий случай: отрезки пересекаются
        if o1 != o2 and o3 != o4:
            # Параметрическое уравнение для пересечения
            denom = ((p1[0] - p2[0]) * (q1[1] - q2[1]) - (p1[1] - p2[1]) * (q1[0] - q2[0]))
            if denom == 0:  # Параллельные отрезки
                return None
            t = ((p1[0] - q1[0]) * (q1[1] - q2[1]) - (p1[1] - q1[1]) * (q1[0] - q2[0])) / denom
            u = -((p1[0] - p2[0]) * (p1[1] - q1[1]) - (p1[1] - p2[1]) * (p1[0] - q1[0])) / denom
            if 0 <= t <= 1 and 0 <= u <= 1:
                x = p1[0] + t * (p2[0] - p1[0])
                y = p1[1] + t * (p2[1] - p1[1])
                return (x, y)
            return None

        # Особый случай: коллинеарные отрезки
        if o1 == 0 and o2 == 0 and o3 == 0 and o4 == 0:
            if on_segment(p1, q1, p2) or on_segment(p1, q2, p2) or on_segment(q1, p1, q2) or on_segment(q1, p2, q2):
                # Найти пересекающиеся точки (для простоты возвращаем одну)
                if on_segment(p1, q1, p2):
                    return q1
                if on_segment(p1, q2, p2):
                    return q2
                if on_segment(q1, p1, q2):
                    return p1
                if on_segment(q1, p2, q2):
                    return p2
            return None

        return None

    def find_intersections(self):
        if len(self.segment_points) != 2:
            messagebox.showinfo("Error", "Need exactly 2 points for the segment!")
            return
        if len(self.points) < 2:
            messagebox.showinfo("Error", "Need at least 2 points for the polygon!")
            return

        self.canvas.delete("intersection")
        self.intersections = []

        segment_p1, segment_p2 = self.segment_points
        n = len(self.points)
        for i in range(n):
            poly_p1 = self.points[i]
            poly_p2 = self.points[(i + 1) % n]  # Следующая точка с замыканием
            intersection = self.find_intersection(segment_p1, segment_p2, poly_p1, poly_p2)
            if intersection:
                self.intersections.append(intersection)
                x, y = intersection
                self.canvas.create_oval(x-4, y-4, x+4, y+4, fill="yellow", tags="intersection")

        if not self.intersections:
            messagebox.showinfo("Intersections", "No intersections found!")
        else:
            messagebox.showinfo("Intersections", f"Found {len(self.intersections)}: ({x, y}) intersection(s)!")

if __name__ == "__main__":
    root = tk.Toplevel()
    app = PolygonEditor(root)
    root.mainloop()