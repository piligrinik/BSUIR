import tkinter as tk
from view import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="#A2B5CD")
    main_window = MainWindow.MainWindow(root)
    root.mainloop()