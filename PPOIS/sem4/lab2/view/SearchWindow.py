import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Optional
from datetime import datetime
import re

import tkcalendar
from tkcalendar import DateEntry

class SearchWindow(tk.Toplevel):
    def __init__(self, root, main_window):
        super().__init__(master=root)
        self.main_window = main_window
        self.title = "Search for soccer players"
        self.configure(background="#BCD2EE")
        self.build_buttons()
        self.date_str = ""

    def build_buttons(self):

        #bith date and name
        ttk.Label(self, text="Player's first name and date of birth:", background="#BCD2EE").pack()
        self.name_entry = ttk.Entry(self, state=tk.DISABLED)
        self.name_entry.pack(pady=(5, 0))
        self.birth_date_entry = DateEntry(self, date_pattern='d-m-yyyy')
        self.birth_date_entry.config(state=tk.DISABLED, background="#3D59AB")
        self.birth_date_entry.pack(pady=(10, 0))
        self.enable_dob_name = tk.BooleanVar()
        self.dob_name_checkbutton = ttk.Checkbutton(self, text="Choose criteria",
                                                    command=lambda: self.switch_state(self.name_entry, self.enable_dob_name, self.birth_date_entry),
                                                    variable=self.enable_dob_name)
        self.dob_name_checkbutton.pack(pady=(10, 0))


        # position
        ttk.Label(self, text="Player's position:", background="#BCD2EE").pack(pady=(20, 0))
        self.position_entry = ttk.Entry(self, state=tk.DISABLED)
        self.position_entry.pack(pady=(5,0))
        self.enable_position = tk.BooleanVar()
        self.position_checkbutton = ttk.Checkbutton(self, text="Choose criteria",
                                                    command=lambda: self.switch_state(self.position_entry,
                                                                                      self.enable_position),
                                                    variable=self.enable_position)
        self.position_checkbutton.pack(pady=(10, 0))


        # squad
        ttk.Label(self, text="Player's squad:", background="#BCD2EE").pack(pady=(20, 0))
        self.squad_entry = ttk.Entry(self, state=tk.DISABLED)
        self.squad_entry.pack(pady=(5, 0))
        self.enable_squad = tk.BooleanVar()
        self.squad_checkbutton = ttk.Checkbutton(self, text="Choose criteria",
                                                    command=lambda: self.switch_state(self.squad_entry,
                                                                                      self.enable_squad),
                                                    variable=self.enable_squad)
        self.squad_checkbutton.pack(pady=(10, 0))


        # soccer team
        ttk.Label(self, text="Player's team:", background="#BCD2EE").pack(pady=(20, 0))
        self.soccer_team_entry = ttk.Entry(self, state=tk.DISABLED)
        self.soccer_team_entry.pack(pady=(5, 0))
        self.enable_soccer_team = tk.BooleanVar()
        self.soccer_team_checkbutton = ttk.Checkbutton(self, text="Choose criteria",
                                                 command=lambda: self.switch_state(self.soccer_team_entry,
                                                                                   self.enable_soccer_team),
                                                 variable=self.enable_soccer_team)
        self.soccer_team_checkbutton.pack(pady=(10, 0))


        # home town
        ttk.Label(self, text="Player's home town:", background="#BCD2EE").pack(pady=(20, 0))
        self.town_entry = ttk.Entry(self, state=tk.DISABLED)
        self.town_entry.pack(pady=(5, 0))
        self.enable_town = tk.BooleanVar()
        self.town_checkbutton = ttk.Checkbutton(self, text="Choose criteria",
                                                       command=lambda: self.switch_state(self.town_entry,
                                                                                         self.enable_town),
                                                       variable=self.enable_town)
        self.town_checkbutton.pack(pady=(10, 0))

        self.apply_btn = ttk.Button(self, text="Apply", command=self.apply_searches)
        self.apply_btn.pack(pady=(10, 10))
        self.apply_btn.bind_all("<Return>", self.apply_searches)



    def switch_state(self, f_entry_state, checkbutton_state, s_entry_state = None):
        state = tk.NORMAL if checkbutton_state.get() else tk.DISABLED
        f_entry_state.config(state=state)
        if s_entry_state:
            s_entry_state.config(state=state)

    def apply_searches(self, event = None):
        criteria = None
        if not (self.enable_dob_name.get() or
                self.enable_position.get() or
                self.enable_squad.get() or
                self.enable_soccer_team.get() or
                self.enable_town.get()):
            messagebox.showerror("No criteria", "None of criteria is selected. Please choose one:")
            return

        if self.name_entry.get() and self.birth_date_entry.get():
            name = self.name_entry.get().strip()
            if not all(re.match("^[A-Za-z]+$", char) for char in name):
                messagebox.showerror("Incorrect name", "Player's first name must be from simbols [A-Z], [a-z] without any spaces")
                self.name_entry.delete(0, 'end')
                self.name_entry.focus_set()
                return
            try:
                date = self.birth_date_entry.get_date()
                self.date_str = date.strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Incorrect date", "It appears, you entered wrong time format."
                                                       " Expected MM-DD-YYYY")
                self.birth_date_entry.delete(0, 'end')
                self.birth_date_entry.focus_set()
                return
            criteria = "name and birthdate"
        elif self.position_entry.get():
            position = self.position_entry.get().strip()
            if not all(re.match("^[A-Za-z]+$", char) for char in position):
                messagebox.showerror("Incorrect position", "Player's position must be from simbols [A-Z], [a-z]")
                self.name_entry.delete(0, 'end')
                self.name_entry.focus_set()
                return
            criteria = "position"
        elif self.squad_entry.get():
            criteria = "squad"
        elif self.soccer_team_entry.get():
            criteria = "soccer team"
        elif self.town_entry.get():
            criteria = "home town"
        else:
            messagebox.showerror("No information where entered", "It appears, you didnt write any information")
            return

        res = self.main_window.search_results(self.name_entry.get(), self.date_str, self.position_entry.get(), self.squad_entry.get(),
                                              self.soccer_team_entry.get(), self.town_entry.get(), criteria)








