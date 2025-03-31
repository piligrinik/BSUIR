import tkinter as tk
from lab1.BSplineCurve import BSplineCurve


class BSplineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("B-Spline")

        self.b_spline = BSplineCurve()
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_canvas_click)

        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        tk.Button(control_frame, text="Очистить", command=self.clear).pack(side=tk.LEFT)
        tk.Button(control_frame, text="Построить", command=self.draw).pack(side=tk.LEFT)

    def on_canvas_click(self, event):
        if len(self.b_spline.points) >= 8:
            return

        x, y = event.x, event.y
        self.b_spline.add_point(x, y)

        # рисунок точки
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')
        # self.canvas.create_text(x, y - 10, text=str(len(self.bezier.points)), fill='blue')


    def draw(self):
        self.canvas.delete("curve")

        if len(self.b_spline.points) != 8:
            return

        points = self.b_spline.calculate_points()

        # Рисуем кривую по точкам
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2,
                                    fill='black', width=2, tags="curve")

    def clear(self):
        self.canvas.delete("all")
        self.b_spline.clear_points()


if __name__ == "__main__":
    root = tk.Tk()
    app = BSplineApp(root)
    root.mainloop()