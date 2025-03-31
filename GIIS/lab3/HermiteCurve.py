import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

class HermiteDrawer():
    def __init__(self, points, derivatives):
        self.points = points
        self.derivatives = derivatives
        self.num_points = 100

    def hermite_interpolation(self, p1, p2, dp1, dp2):
        t = np.linspace(0, 1, self.num_points)
        h00 = 2 * t**3 - 3 * t**2 + 1
        h10 = t**3 - 2 * t**2 + t
        h01 = -2 * t**3 + 3 * t**2
        h11 = t**3 - t**2

        x = h00 * p1[0] + h10 * dp1[0] + h01 * p2[0] + h11 * dp2[0]
        y = h00 * p1[1] + h10 * dp1[1] + h01 * p2[1] + h11 * dp2[1]

        return np.column_stack((x, y))

    def interpolate_segments(self):
        curve = []
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            dp1 = self.derivatives[i]
            dp2 = self.derivatives[i + 1]
            segment = self.hermite_interpolation(p1, p2, dp1, dp2)
            curve.extend(segment)
        return np.array(curve)

    def attach_point(self, entries):
        new_point = [int(entry.get()) for entry in entries[:2]]
        new_derivative = [int(entry.get()) for entry in entries[2:]]
        self.points.append(np.array(new_point))
        self.derivatives.append(np.array(new_derivative))

    def adjust_points(self, entries_x, entries_y, entries_dx, entries_dy):
        for i, point in enumerate(self.points):
            self.points[:][i][0] = entries_x[i].get()
            self.points[:][i][1] = entries_y[i].get()
        for i, point in enumerate(self.derivatives):
            self.derivatives[:][i][0] = entries_dx[i].get()
            self.derivatives[:][i][1] = entries_dy[i].get()


def adjustment():
    # entry_points = np.zeros((len(points), len(points[0])), dtype=int)
    entries_x = []
    entries_y = []
    entries_dx = []
    entries_dy = []
    root2 = tk.Toplevel(root)
    root2.title("Adjustment")
    label_x = tk.Label(root2, text="Px")
    label_x.place(relx=0.1, rely=0, anchor="nw")
    for i in range(len(points)):
        entry1 = tk.Entry(root2, width=5)
        entry1.insert(0, points[:][i][0])
        entry1.place(relx=0.1, rely=0.1 + i * 0.1, anchor="nw")
        entries_x.append(entry1)
        # entry_points = np.append(entry_points, [points[:][i][0]], axis=1)
    label_y = tk.Label(root2, text="Py")
    label_y.place(relx=0.3, rely=0, anchor="nw")
    for i in range(len(points)):
        entry2 = tk.Entry(root2, width=5)
        entry2.insert(0, points[:][i][1])
        entry2.place(relx=0.3, rely=0.1 + i * 0.1, anchor="nw")
        entries_y.append(entry2)
    label_dx = tk.Label(root2, text="Rx")
    label_dx.place(relx=0.5, rely=0, anchor="nw")
    for i in range(len(derivatives)):
        entry3 = tk.Entry(root2, width=5)
        entry3.insert(0, derivatives[:][i][0])
        entry3.place(relx=0.5, rely=0.1 + i * 0.1, anchor="nw")
        entries_dx.append(entry3)
    label_dy = tk.Label(root2, text="Ry")
    label_dy.place(relx=0.7, rely=0, anchor="nw")
    for i in range(len(derivatives)):
        entry4 = tk.Entry(root2, width=5)
        entry4.insert(0, derivatives[:][i][1])
        entry4.place(relx=0.7, rely=0.1 + i * 0.1, anchor="nw")
        entries_dy.append(entry4)
    submit_bttn = ttk.Button(root2, text="Submit", command=lambda: adjust_points(entries_x, entries_y,
                                                                                 entries_dx, entries_dy))
    submit_bttn.place(relx=0.5, rely=0.8 ,anchor="s")



def draw_curves():
    canvas.delete("all")
    hermite_drawer = HermiteDrawer(points, derivatives)
    curve = hermite_drawer.interpolate_segments()
    for i in range(len(curve) - 1):
        x0, y0 = curve[i]
        x1, y1 = curve[i + 1]
        canvas.create_line(x0 * 100, y0 * 100, x1 * 100, y1 * 100, fill="black")

    for p in points:
        canvas.create_oval(p[0] * 100 - 3, p[1] * 100 - 3, p[0] * 100 + 3, p[1] * 100 + 3, fill="red")


if __name__ == "__main__":
    draw_curves()
    root.mainloop()
