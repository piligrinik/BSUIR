import tkinter as tk
import random
import math
from heapq import heappush, heappop


class DelaunayAlgorithm:
    def __init__(self, points):
        self.points = points

    def run(self):
        def in_circle(p, a, b, c):
            ax, ay = a[0] - p[0], a[1] - p[1]
            bx, by = b[0] - p[0], b[1] - p[1]
            cx, cy = c[0] - p[0], c[1] - p[1]
            det = (ax ** 2 + ay ** 2) * (bx * cy - by * cx) - (bx ** 2 + by ** 2) * (ax * cy - ay * cx) + (
                        cx ** 2 + cy ** 2) * (ax * by - ay * bx)
            return det > 0

        def find_supertriangle(points):
            min_x = min(x for x, y in points)
            max_x = max(x for x, y in points)
            min_y = min(y for x, y in points)
            max_y = max(y for x, y in points)
            dx, dy = max_x - min_x, max_y - min_y
            max_d = max(dx, dy) * 3
            mid_x, mid_y = (min_x + max_x) / 2, (min_y + max_y) / 2
            return [
                (mid_x - max_d, mid_y - max_d),
                (mid_x + max_d, mid_y - max_d),
                (mid_x, mid_y + max_d)
            ]

        if len(self.points) < 3:
            return []

        supertri = find_supertriangle(self.points)
        triangles = [supertri]
        temp_points = self.points + supertri

        for p in self.points:
            bad_triangles = []
            for t in triangles:
                if in_circle(p, t[0], t[1], t[2]):
                    bad_triangles.append(t)

            polygon = []
            for t in bad_triangles:
                for i in range(3):
                    edge = (t[i], t[(i + 1) % 3])
                    shared = False
                    for t2 in bad_triangles:
                        if t2 != t and edge[0] in t2 and edge[1] in t2:
                            shared = True
                            break
                    if not shared:
                        polygon.append(edge)

            triangles = [t for t in triangles if t not in bad_triangles]
            for edge in polygon:
                triangles.append([edge[0], edge[1], p])

        triangles = [t for t in triangles if not any(p in supertri for p in t)]
        edges = set()
        for t in triangles:
            edges.add(tuple(sorted([t[0], t[1]])))
            edges.add(tuple(sorted([t[1], t[2]])))
            edges.add(tuple(sorted([t[2], t[0]])))

        return list(edges)


