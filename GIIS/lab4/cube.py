import numpy as np
import tkinter as tk
from math import cos, sin, radians, tan


class Cube:
    def __init__(self, vertices, edges):
        self.vertices = np.array(vertices, dtype=float)
        self.edges = edges
        self.original_vertices = self.vertices.copy()

    def reset(self):
        self.vertices = self.original_vertices.copy()

    def translate(self, dx, dy, dz):
        translation_matrix = np.array([
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1]
        ])
        self.apply_transform(translation_matrix)

    def rotate_x(self, angle):
        angle = radians(angle)
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])
        self.apply_transform(rotation_matrix)

    def rotate_y(self, angle):
        angle = radians(angle)
        rotation_matrix = np.array([
            [cos(angle), 0, sin(angle), 0],
            [0, 1, 0, 0],
            [-sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])
        self.apply_transform(rotation_matrix)

    def rotate_z(self, angle):
        angle = radians(angle)
        rotation_matrix = np.array([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.apply_transform(rotation_matrix)

    def scale(self, sx, sy, sz):
        scaling_matrix = np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])
        self.apply_transform(scaling_matrix)

    def apply_perspective(self, distance):
        if distance <= 0:
            distance = 0.001
        perspective_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -1 / distance, 1]
        ])
        self.apply_transform(perspective_matrix)

    def apply_transform(self, matrix):
        homogeneous_vertices = np.hstack((self.vertices, np.ones((len(self.vertices), 1))))
        transformed_vertices = np.dot(homogeneous_vertices, matrix.T)

        # Перспективное деление
        w = transformed_vertices[:, 3]
        self.vertices = transformed_vertices[:, :3] / w[:, np.newaxis]

    def get_projected_vertices(self, width, height):
        projected = []
        scale = min(width, height) / 3

        for vertex in self.vertices:
            # Переводим в координаты экрана
            x = vertex[0] * scale + width / 2
            y = -vertex[1] * scale + height / 2
            projected.append((x, y))

        return projected


def read_cube_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    vertices = []
    edges = []

    for line in lines:
        if line.startswith('v '):
            parts = line.strip().split()
            vertices.append([float(parts[1])/1.5, float(parts[2])/1.5, float(parts[3])/1.5])
        elif line.startswith('e '):
            parts = line.strip().split()
            edges.append((int(parts[1]), int(parts[2])))

    return Cube(vertices, edges)


class CubeApp():
    def __init__(self, root, cube):
        self.root = root
        self.cube = cube
        self.width = 1000
        self.height = 800

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='white')
        self.canvas.pack(side=tk.LEFT)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.create_controls()
        self.draw_cube()

    def create_controls(self):
        reset_btn = tk.Button(self.control_frame, text="Сброс", command=self.reset_cube)
        reset_btn.pack(fill=tk.X, pady=5)

        # перемещение
        tk.Label(self.control_frame, text="Перемещение").pack()
        self.translate_x = self.create_slider("X", -2, 2, 0, resolution=0.1)
        self.translate_y = self.create_slider("Y", -2, 2, 0, resolution=0.1)
        self.translate_z = self.create_slider("Z", -5, 5, 0, resolution=0.1)

        # поворот
        tk.Label(self.control_frame, text="Поворот").pack()
        self.rotate_x = self.create_slider("X (град)", -180, 180, 0)
        self.rotate_y = self.create_slider("Y (град)", -180, 180, 0)
        self.rotate_z = self.create_slider("Z (град)", -180, 180, 0)

        # масштабирование
        tk.Label(self.control_frame, text="Масштабирование").pack()
        self.scale = self.create_slider("Масштаб", 0.1, 2, 1, resolution=0.1)

        # перспектива
        tk.Label(self.control_frame, text="Перспектива").pack()
        self.perspective = self.create_slider("Дистанция", 1, 10, 5, resolution=0.1)

    def create_slider(self, label, from_, to, default, resolution=1):
        frame = tk.Frame(self.control_frame)
        frame.pack(fill=tk.X, pady=2)

        tk.Label(frame, text=label, width=12).pack(side=tk.LEFT)
        scale = tk.Scale(frame, from_=from_, to=to, orient=tk.HORIZONTAL,
                         resolution=resolution, command=lambda _: self.update_cube())
        scale.set(default)
        scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        return scale

    def reset_cube(self):
        self.cube.reset()
        self.translate_x.set(0)
        self.translate_y.set(0)
        self.translate_z.set(0)
        self.rotate_x.set(0)
        self.rotate_y.set(0)
        self.rotate_z.set(0)
        self.scale.set(1)
        self.perspective.set(5)
        self.draw_cube()

    def update_cube(self):
        self.cube.reset()

        # порядок:
        # масштабирование
        # поворот
        # перемещение
        # перспектива

        scale_val = float(self.scale.get())
        self.cube.scale(scale_val, scale_val, scale_val)

        self.cube.rotate_x(float(self.rotate_x.get()))
        self.cube.rotate_y(float(self.rotate_y.get()))
        self.cube.rotate_z(float(self.rotate_z.get()))

        self.cube.translate(
            float(self.translate_x.get()),
            float(self.translate_y.get()),
            float(self.translate_z.get())
        )

        self.cube.apply_perspective(float(self.perspective.get()))

        self.draw_cube()

    def draw_cube(self):
        self.canvas.delete("all")
        vertices = self.cube.get_projected_vertices(self.width, self.height)

        # Рисуем ребра
        for edge in self.cube.edges:
            x1, y1 = vertices[edge[0]]
            x2, y2 = vertices[edge[1]]
            self.canvas.create_line(x1, y1, x2, y2, fill='grey', width=2)


def main():
    cube_filename = "cube.txt"

    try:
        cube = read_cube_from_file(cube_filename)
    except FileNotFoundError:
        # Куб по умолчанию (1x1x1)
        vertices = [
            [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5]
        ]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Нижняя грань
            (4, 5), (5, 6), (6, 7), (7, 4),  # Верхняя грань
            (0, 4), (1, 5), (2, 6), (3, 7)  # Боковые ребра
        ]
        cube = Cube(vertices, edges)

        with open(cube_filename, 'w') as f:
            for v in vertices:
                f.write(f"v {v[0]} {v[1]} {v[2]}\n")
            for e in edges:
                f.write(f"e {e[0]} {e[1]}\n")

    root = tk.Tk()
    root.title("3D Кубик с правильными преобразованиями")
    app = CubeApp(root, cube)
    root.mainloop()


if __name__ == "__main__":
    main()