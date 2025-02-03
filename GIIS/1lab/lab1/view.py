import tkinter as tk
from tkinter import ttk
from lab1.lines import LineDrawer

root = tk.Tk()
root.title("Graphic editor")
root.geometry("800x600")
root.configure(bg='lavenderblush2')
lineDrawer = LineDrawer()



label = tk.Label(root, text="Welcome to\n graphic editor!", bg="lavenderblush2",  font=("Segoe UI", 20, "bold"))
label.place(relx=0.65, rely=0.5, anchor="center")

buttons = ["Draw the line", "smth", "smth", "smth", "smth", "smth"]
for i, btn_text in enumerate(buttons):
    btn = ttk.Button(root, text=btn_text, command=lambda: open_coord_window(), width=25)
    btn.place(relx=0.1, rely=0.1 + i * 0.15, anchor="w")

def open_new_window(x0, y0, x1, y1, cell_size):
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
    return 0

def open_coord_window():
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
    # x0 = int(entry_x0.get())
    # y0 = int(entry_y0.get())
    # x1 = int(entry_x1.get())
    # y1 = int(entry_y1.get())
    # cell_size = int(entry_cell_size.get())

    draw_button = ttk.Button(root2, text="Draw the line",
                             command=lambda: open_new_window(int(entry_x0.get()), int(entry_y0.get()),
                                                             int(entry_x1.get()), int(entry_y1.get()), int(entry_cell_size.get())))
    draw_button.grid(row=5, columnspan=2)

    return 0



if __name__ == "__main__":
    root.mainloop()
