import tkinter as tk
from lab1.HermiteCurve import HermiteDrawer
import numpy as np
from tkinter import ttk

class HermiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Hermite's Interpolation"
        self.hermite_coords()


    def hermite_coords(self):
        label_x = tk.Label(self.root, text="Px")
        label_x.place(relx=0.1, rely=0.1, anchor="nw")
        label_y = tk.Label(self.root, text="Py")
        label_y.place(relx=0.3, rely=0.1, anchor="nw")
        label_dx = tk.Label(self.root, text="Rx")
        label_dx.place(relx=0.5, rely=0.1, anchor="nw")
        label_dy = tk.Label(self.root, text="Ry")
        label_dy.place(relx=0.7, rely=0.1, anchor="nw")
        entries1 = []
        entries2 = []
        for i in range(4):
            entry = tk.Entry(self.root, width=5)
            entry.place(relx=0.1 + i * 0.2, rely=0.2, anchor="nw")
            entries1.append(entry)
        for i in range(4):
            entry = tk.Entry(self.root, width=5)
            entry.place(relx=0.1 + i * 0.2, rely=0.4, anchor="nw")
            entries2.append(entry)
        submit_bttn = ttk.Button(self.root, text="Submit", command=lambda: self.hermite_window(entries1, entries2))
        submit_bttn.place(relx=0.5, rely=0.8, anchor="s")

    def hermite_window(self, entries1, entries2):
        if not hasattr(self.hermite_window, "root1") or not self.hermite_window.root1.winfo_exists():
            points = []
            derivatives = []
            new_point1 = [int(entry.get()) for entry in entries1[:2]]
            new_derivative1 = [int(entry.get()) for entry in entries1[2:]]
            new_point2 = [int(entry.get()) for entry in entries2[:2]]
            new_derivative2 = [int(entry.get()) for entry in entries2[2:]]
            points.append(np.array(new_point1))
            derivatives.append(np.array(new_derivative1))
            points.append(np.array(new_point2))
            derivatives.append(np.array(new_derivative2))
            self.hermite_drawer = HermiteDrawer(points, derivatives)
            hermite_canvas = tk.Toplevel(self.root)
            hermite_canvas.title("Hermit's interpolation")
            self.canvas = tk.Canvas(hermite_canvas, width=900, height=800, bg="white")
            self.canvas.pack()
            menu = tk.Menu(hermite_canvas)
            menu.add_cascade(label="Корректировка", command=lambda: self.adjustment(points, derivatives))
            menu.add_cascade(label="Состыковка", command=lambda: self.attachment())
            hermite_canvas.config(menu=menu)
            self.hermite_draw()

    def hermite_draw(self):
        self.canvas.delete("all")
        curve = self.hermite_drawer.interpolate_segments()
        for i in range(len(curve) - 1):
            x0, y0 = curve[i]
            x1, y1 = curve[i + 1]
            self.canvas.create_line(x0 * 100, y0 * 100, x1 * 100, y1 * 100, fill="black")
        # points red
        for p in self.hermite_drawer.points:
            self.canvas.create_oval(p[0] * 100 - 3, p[1] * 100 - 3, p[0] * 100 + 3, p[1] * 100 + 3, fill="red")

    def attachment(self):
        root2 = tk.Toplevel(self.root)
        root2.title("Attachment")
        label_x = tk.Label(root2, text="Px")
        label_x.place(relx=0.1, rely=0.1, anchor="nw")
        label_y = tk.Label(root2, text="Py")
        label_y.place(relx=0.3, rely=0.1, anchor="nw")
        label_dx = tk.Label(root2, text="Rx")
        label_dx.place(relx=0.5, rely=0.1, anchor="nw")
        label_dy = tk.Label(root2, text="Ry")
        label_dy.place(relx=0.7, rely=0.1, anchor="nw")
        entries = []
        for i in range(4):
            entry = tk.Entry(root2, width=5)
            entry.place(relx=0.1 + i * 0.2, rely=0.2, anchor="nw")
            entries.append(entry)
        submit_bttn = ttk.Button(root2, text="Submit", command=lambda: [self.hermite_drawer.attach_point(entries),
                                                                        self.hermite_draw()])
        submit_bttn.place(relx=0.5, rely=0.8, anchor="s")
        # submit_bttn.bind("<ButtonPress>", lambda: hermite_drawer.attach_point(entries))
        # submit_bttn.bind("<ButtonRelease>", lambda: hermite_draw(canvas))

    def adjustment(self, points, derivatives):
        # entry_points = np.zeros((len(points), len(points[0])), dtype=int)
        entries_x = []
        entries_y = []
        entries_dx = []
        entries_dy = []
        root2 = tk.Toplevel(self.root)
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
        submit_bttn = ttk.Button(root2, text="Submit",
                                 command=lambda: [self.hermite_drawer.adjust_points(entries_x, entries_y,
                                                                               entries_dx, entries_dy),
                                                  self.hermite_draw()])
        submit_bttn.place(relx=0.5, rely=0.8, anchor="s")