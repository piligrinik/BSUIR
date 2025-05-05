import tkinter as tk
from DelaunayAlgorithm import DelaunayAlgorithm


class DelaunayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delaunay Triangulation and Voronoi Diagram with Beachline")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.points = []
        self.mode = None
        self.sweep_y = 300  # Фиксированная позиция линии зачистки для отображения

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.clear_points)

        button_frame = tk.Frame(root)
        button_frame.pack()
        tk.Button(button_frame, text="Calculation", command=self.set_delaunay_mode).pack(side=tk.LEFT)

        self.draw()


    def set_delaunay_mode(self):
        self.mode = "delaunay"
        self.draw()


    def add_point(self, event):
        self.points.append((event.x, event.y))
        self.draw()

    def clear_points(self, event):
        self.points = []
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        # Отрисовка точек
        for x, y in self.points:
            self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

        fortune = None

        if self.mode:
            if len(self.points) >= 3 and self.mode in "delaunay":
                delaunay = DelaunayAlgorithm(self.points)
                delaunay_edges = delaunay.run()
                for (p1, p2) in delaunay_edges:
                    self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="blue")


if __name__ == "__main__":
    root = tk.Tk()
    app = DelaunayApp(root)
    root.mainloop()