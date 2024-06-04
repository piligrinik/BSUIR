import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Optional
from datetime import datetime
import re
from tkcalendar import DateEntry


class AddWindow(tk.Toplevel):
    def __init__(self, root, main_window):
        super().__init__(master=root)
        self.main_window = main_window
        self.root = root
        self.title = "Add player"
        self.configure(background="#BCD2EE")
        self.geometry("200x600")
        self.build_btns()
        self.date_str = ""

    def build_btns(self):
        ttk.Label(self, text="Full name:", background="#BCD2EE").pack(pady=(5,0))
        self.full_name_entry = ttk.Entry(self)
        self.full_name_entry.pack(pady=(5, 20))
        ttk.Label(self, text= "Birth date: ", background="#BCD2EE").pack()
        self.birth_date_entry = DateEntry(self, date_pattern='d-m-yyyy')
        self.birth_date_entry.config(background="#A2B5CD")
        self.birth_date_entry.pack(pady=(5, 20))
        ttk.Label(self, text="Soccer team:", background="#BCD2EE").pack()
        self.soccer_team_entry = ttk.Entry(self)
        self.soccer_team_entry.pack(pady=(5, 20))
        ttk.Label(self, text="Home town:", background="#BCD2EE").pack()
        self.home_town_entry = ttk.Entry(self)
        self.home_town_entry.pack(pady=(5, 20))
        ttk.Label(self, text="Squad: ", background="#BCD2EE").pack()
        self.squad_entry = ttk.Entry(self)
        self.squad_entry.pack(pady=(5, 20))
        ttk.Label(self, text="Position: ", background="#BCD2EE").pack()
        self.position_entry = ttk.Entry(self)
        self.position_entry.pack(pady=(5, 20))

        self.add_btn = ttk.Button(self, text="Add", command=self.add_player)
        self.add_btn.pack(pady=(10, 0))
        self.add_btn.bind_all("<Return>", self.add_player)

    def add_player(self, event = None):
        full_name = self.full_name_entry.get().strip()
        birth_date = self.birth_date_entry.get_date()
        soccer_team = self.soccer_team_entry.get().strip()
        home_town = self.home_town_entry.get().strip()
        position = self.position_entry.get().strip()
        squad = self.squad_entry.get().strip()
        if not all((full_name, birth_date, soccer_team, home_town, squad, position)):
            messagebox.showerror("Lack of information", "It appears, some information is missing")
            return
        try:
            self.date_str = birth_date.strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Wrong data format", "It appears, you entered wrong time format."
                                                      " Expected MM-DD-YYYY")
            self.birth_date_entry.delete(0, 'end')
            self.birth_date_entry.focus_set()
            return
        if not all(re.match("^[A-Za-z]+$", word) for word in full_name.split()):
            messagebox.showerror("Wrong name format", "Player's full name must be from simbols [A-Z], [a-z].")
            self.patient_name_entry.delete(0, 'end')
            self.patient_name_entry.focus_set()
            return
        if self.main_window.file.find_player(full_name, birth_date, soccer_team, home_town, squad, position):
            messagebox.showerror("Player exists", "It appears, this player already exists")
            self.full_name_entry.delete(0, 'end')
            self.soccer_team_entry.delete(0, 'end')
            self.home_town_entry.delete(0, 'end')
            self.position_entry.delete(0, 'end')
            self.squad_entry.delete(0, 'end')
            self.full_name_entry.focus_set()
            return
        self.main_window.file.add_player(full_name, self.date_str, soccer_team, home_town, squad, position)
        self.main_window.update_records()
        messagebox.showinfo("Success!", "Player was successfully added.")
        self.destroy()



