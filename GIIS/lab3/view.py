import tkinter as tk
from tkinter import ttk
import numpy as np
from lab1.lines import LineDrawer
from lab1.circle import CircleDrawer
from lab1.ellipse import EllipseDrawer
from lab1.hyperbola import HyperbolaDrawer
from lab1.parabola import ParabolaDrawer
from lab1.HermiteCurve import HermiteDrawer
from lab1.HermiteView import HermiteApp
from lab1.BezierView import BezierApp
from lab1.BSplineView import BSplineApp



root = tk.Tk()
root.title("Graphic editor")
root.geometry("800x600")
root.configure(bg='lavenderblush2')
lineDrawer = LineDrawer()



label = tk.Label(root, text="Welcome to\n graphic editor!", bg="lavenderblush2",  font=("Segoe UI", 20, "bold"))
label.place(relx=0.65, rely=0.5, anchor="center")



buttons = ["Draw the line", "Draw the circle", "Draw the ellipse", "Draw the hyperbola", "Draw the parabola", "Draw the curve",
           "smth", "smth"]
button_lines = ttk.Button(root, text=buttons[0], command=lambda: open_lines_window(), width=28)
button_lines.place(relx=0.1, rely=0.1, anchor="w")
button_circle = ttk.Button(root, text=buttons[1], command=lambda: open_circle_coords(), width=28)
button_circle.place(relx=0.1, rely=0.2, anchor="w")
button_ellipse = ttk.Button(root, text=buttons[2], command=lambda: open_ellipse_coords(), width=28)
button_ellipse.place(relx=0.1, rely=0.3, anchor="w")
button_hyperbola = ttk.Button(root, text=buttons[3], command=lambda: open_hyperbola_coords(), width=28)
button_hyperbola.place(relx=0.1, rely=0.4, anchor="w")
button_parabola = ttk.Button(root, text=buttons[4], command=lambda: open_parabola_coords(), width=28)
button_parabola.place(relx=0.1, rely=0.5, anchor="w")
button_curve = ttk.Button(root, text=buttons[5], command=lambda: open_curves_window(), width=28)
button_curve.place(relx=0.1, rely=0.6, anchor="w")


for i, btn_text in enumerate(buttons[6:]):
    btn = ttk.Button(root, text=btn_text, width=28)
    btn.place(relx=0.1, rely=0.7 + i * 0.1, anchor="w")

def open_lines_window(x0, y0, x1, y1, cell_size):
    new_window = tk.Toplevel(root)
    new_window.title("Method selection")

    button1 = ttk.Button(new_window, text="DDA method", command=lambda: lineDrawer.draw_line(1, x0,y0, x1, y1, cell_size))
    button1.pack(pady=10)
    debug_button1 = ttk.Button(new_window, text="Debug of DDA", command=lambda: lineDrawer.start_debug(1, x0,y0, x1, y1, cell_size))
    debug_button1.pack(pady=10)

    button2 = ttk.Button(new_window, text="Bresenham's method", command=lambda: lineDrawer.draw_line(2, x0,y0, x1, y1, cell_size))
    button2.pack(pady=10)
    debug_button2 = ttk.Button(new_window, text="Debug of Bresehham's",
                               command=lambda: lineDrawer.start_debug(2, x0, y0, x1, y1, cell_size))
    debug_button2.pack(pady=10)

    button3 = ttk.Button(new_window, text="Wu's method", command=lambda: lineDrawer.draw_line(3, x0,y0, x1, y1, cell_size))
    button3.pack(pady=10)
    debug_button3 = ttk.Button(new_window, text="Debug of Wu's", command=lambda: lineDrawer.start_debug(3, x0, y0, x1, y1, cell_size))
    debug_button3.pack(pady=10)
    return None

def open_lines_coord_window():
    root2 = tk.Toplevel(root)
    root2.title("Graphic editor")

    tk.Label(root2, text="x0").grid(row=0, column=0)
    entry_x0 = tk.Entry(root2)
    entry_x0.grid(row=0, column=1)

    tk.Label(root2, text="y0").grid(row=1, column=0)
    entry_y0 = tk.Entry(root2)
    entry_y0.grid(row=1, column=1)

    tk.Label(root2, text="x1").grid(row=2, column=0)
    entry_x1 = tk.Entry(root2)
    entry_x1.grid(row=2, column=1)

    tk.Label(root2, text="y1").grid(row=3, column=0)
    entry_y1 = tk.Entry(root2)
    entry_y1.grid(row=3, column=1)

    tk.Label(root2, text="Cell size").grid(row=4, column=0)
    entry_cell_size = tk.Entry(root2)
    entry_cell_size.grid(row=4, column=1)

    draw_button = ttk.Button(root2, text="Draw the line",
                             command=lambda: open_lines_window(int(entry_x0.get()), int(entry_y0.get()),
                                                             int(entry_x1.get()), int(entry_y1.get()), int(entry_cell_size.get())))
    draw_button.grid(row=5, columnspan=2)

    return None

def open_circle_coords():
    root2 = tk.Toplevel(root)
    root2.title("Circle generation")

    tk.Label(root2, text="R: ").grid(row=0, column=0)
    entry_r = tk.Entry(root2)
    entry_r.grid(row=0, column=1)

    draw_bttn = ttk.Button(root2, text="Generate",
                             command=lambda: circle_generation(1, int(entry_r.get())))
    draw_bttn.grid(row=1, columnspan=2)

    debug_button = ttk.Button(root2, text="Generation debug",
                             command=lambda: circle_generation(2, int(entry_r.get())))
    debug_button.grid(row=2, columnspan=2)
    return None

def circle_generation(k: int, r: int):
    circle_drawer = CircleDrawer(r)
    match(k):
        case 1: circle_drawer.draw_circle()
        case 2: circle_drawer.start_debug()
        case _: circle_drawer.draw_circle()
    return None

def open_ellipse_coords():
    root2 = tk.Toplevel(root)
    root2.title("Ellipse generation")

    tk.Label(root2, text="a: ").grid(row=0, column=0)
    entry_a = tk.Entry(root2)
    entry_a.grid(row=0, column=1)
    tk.Label(root2, text="b: ").grid(row=1, column=0)
    entry_b = tk.Entry(root2)
    entry_b.grid(row=1, column=1)

    draw_bttn = ttk.Button(root2, text="Generate",
                           command=lambda: ellipse_generation(1, int(entry_a.get()), int(entry_b.get())))
    draw_bttn.grid(row=2, columnspan=2)

    debug_button = ttk.Button(root2, text="Generation debug",
                              command=lambda: ellipse_generation(2, int(entry_a.get()), int(entry_b.get())))
    debug_button.grid(row=3, columnspan=2)
    return None

def ellipse_generation(k: int, a: int, b: int):
    ellipse_drawer = EllipseDrawer(a, b)
    match (k):
        case 1:
            ellipse_drawer.draw_ellipse()
        case 2:
            ellipse_drawer.start_debug()
        case _:
            ellipse_drawer.draw_ellipse()
    return None


def open_hyperbola_coords():
    root2 = tk.Toplevel(root)
    root2.title("Hyperbola generation")

    tk.Label(root2, text="p: ").grid(row=0, column=0)
    entry_p = tk.Entry(root2)
    entry_p.grid(row=0, column=1)

    draw_bttn = ttk.Button(root2, text="Generate",
                           command=lambda: hyperbola_generation(1, int(entry_p.get())))
    draw_bttn.grid(row=1, columnspan=2)

    debug_button = ttk.Button(root2, text="Generation debug",
                              command=lambda: hyperbola_generation(2, int(entry_p.get())))
    debug_button.grid(row=2, columnspan=2)
    return None


def hyperbola_generation(k: int, p: int):
    hyperbola_drawer = HyperbolaDrawer(p)
    match (k):
        case 1:
            hyperbola_drawer.draw_hyperbola()
        case 2:
            hyperbola_drawer.start_debug()
        case _:
            hyperbola_drawer.draw_hyperbola()
    return None


def open_parabola_coords():
    root2 = tk.Toplevel(root)
    root2.title("Parabola generation")

    tk.Label(root2, text="p: ").grid(row=0, column=0)
    entry_p = tk.Entry(root2)
    entry_p.grid(row=0, column=1)

    draw_bttn = ttk.Button(root2, text="Generate",
                           command=lambda: parabola_generation(1, int(entry_p.get())))
    draw_bttn.grid(row=1, columnspan=2)

    debug_button = ttk.Button(root2, text="Generation debug",
                              command=lambda: parabola_generation(2, int(entry_p.get())))
    debug_button.grid(row=2, columnspan=2)
    return None


def parabola_generation(k: int, p: int):
    parabola_drawer = ParabolaDrawer(p)
    match (k):
        case 1:
            parabola_drawer.draw_parabola()
        case 2:
            parabola_drawer.start_debug()
        case _:
            parabola_drawer.draw_parabola()
    return None

def open_curves_window():
    root3 = tk.Toplevel(root)
    root3.title("Curve generation")
    root3.configure(bg='lavenderblush2')
    root3.geometry("300x300")
    tk.Label(root3, text="Please, select the method:", bg='lavenderblush2').pack(anchor="c")
    bttn_hermite = ttk.Button(root3, text="Hermite's interpolation", command=hermite_window, width=28)
    bttn_hermite.pack(padx=50, pady=30, anchor="c")
    bttn_bezier = ttk.Button(root3, text="Bezier curve", command=bezier_window, width=28)
    bttn_bezier.pack(padx=50, pady=31, anchor="c")
    bttn_spline = ttk.Button(root3, text="B-Spline", command=spline_window, width=28)
    bttn_spline.pack(padx=50, pady=32, anchor="c")

def hermite_window():
    root_hermite = tk.Toplevel(root)
    hermite_drawer = HermiteApp(root_hermite)

def bezier_window():
    root_bezier = tk.Toplevel(root)
    bezier_drawer = BezierApp(root_bezier)

def spline_window():
    root_spline = tk.Toplevel(root)
    bezier_drawer = BSplineApp(root_spline)



if __name__ == "__main__":
    root.mainloop()
