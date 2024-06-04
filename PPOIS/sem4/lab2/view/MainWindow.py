import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from model.FileProcessor import FileProcessor
from .SearchWindow import SearchWindow
from controller.SearchCriteria import SearchCriteria
from .SearchResultWindow import SearchResultWindow
from .AddWindow import AddWindow
from.DeleteWindow import DeleteWindow



# MAKE CONTROLLER BUILD VIEW IN THE MAIN FUNCTION THROUGH ITS CLASS
# BUILD THOSE INSTANCES


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Soccer Players')
        self.player_table = None
        self.menu = None
        self.first_page_button = None
        self.last_page_button = None
        self.next_page_button = None
        self.previous_page_button = None
        self.page_quantity = None
        self.file = None
        self.players_per_page= 10
        self.current_page_num = 0
        self.create_view()

    def create_view(self):
        # table
        columns = ["Full Name", "Birth Date", "Soccer Team", "Home Town", "Squad", "Position"]
        self.player_table = ttk.Treeview(self.root, columns=columns, show="headings")
        self.player_table.grid(row=0, column=0, padx=[10, 10], pady=10, columnspan=3)
        self.player_table.configure(height=20)
        self.player_table.heading("Full Name", text="Full Name")
        self.player_table.heading("Birth Date", text="Birth Date")
        self.player_table.heading("Soccer Team", text="Soccer Team")
        self.player_table.heading("Home Town", text="Home Town")
        self.player_table.heading("Squad", text="Squad")
        self.player_table.heading("Position", text="Position")
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.player_table.yview)
        scrollbar.grid(row=0, column=2, sticky='nse')



        # page navigation
        self.first_page_button = ttk.Button(self.root, text="Last page", command= self.turn_last_page)
        self.first_page_button.grid(row=2, column=2,padx= 50,pady=5, sticky="e")
        self.last_page_button = ttk.Button(self.root, text="First page", command=self.turn_first_page)
        self.last_page_button.grid(row=2, column=0, padx=50, pady=5, sticky="w")
        self.previous_page_button = ttk.Button(self.root, text= "Previous page", command= self.turn_previous_page)
        self.previous_page_button.grid(row=2, column=0, pady=5, sticky="e")
        self.next_page_button = ttk.Button(self.root, text="Next page", command=self.turn_next_page)
        self.next_page_button.grid(row=2, column=2, pady=5, sticky="w")

        self.current_page_txt = ttk.Label(self.root, text="Current page: 1", background="#A2B5CD")
        self.current_page_txt.grid(row=1, column= 2)

        # page quantity
        self.players_p_page_var = tk.StringVar(value = 10)
        self.players_quantity = ttk.Spinbox(self.root, from_=5, to=60, increment=5, width=3,
                                            textvariable=self.players_p_page_var, command=self.set_p_per_page, state=tk.DISABLED)
        self.players_quantity.configure(background="#A2B5CD", width=15)
        self.players_quantity.grid(row=2, column=1, padx=(1, 1), pady=5)
        self.players_quantity_text = ttk.Label(self.root, text="Player quantity per page:", background="#A2B5CD")
        self.players_quantity_text.grid(row=1, column= 1, pady=10)

        self.menu = tk.Menu()
        self.menu.add_command(label="Add" ,comman=self.add_player)
        self.menu.add_command(label="Search", command=self.search_window)
        self.menu.add_command(label="Delete", command=self.delete_players)
        self.menu.add_command(label="Open file", command=self.open_file)
        self.root.config(menu=self.menu)

    def open_file(self):
        filename = filedialog.askopenfilename(title='Open file', filetypes=[('XML files', '*.xml')])
        if filename is not None and len(filename) > 0:
            self.file = None
            self.file = FileProcessor(filename)
            self.update_records()


    def update_records(self):
        for item in self.player_table.get_children():
            self.player_table.delete(item)
        start = self.current_page_num * self.players_per_page
        end = start + self.players_per_page
        for player in self.file.get_players_from_file()[start:end]:
            self.player_table.insert("", 'end', values=player.get_player_info())
        self.current_page_txt.config(text=f"Current page: {self.current_page_num + 1}")
        self.players_quantity["state"] = tk.NORMAL

    def turn_next_page(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to turn pages", title="No pages found")
        else:
            pages = len(self.file.get_players_from_file()) / self.players_per_page
            if (self.current_page_num + 1) < pages:
                self.current_page_num +=1
                self.update_records()

    def turn_previous_page(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to turn pages", title="No pages found")
        else:
            if self.current_page_num > 0:
                self.current_page_num -=1
                self.update_records()

    def turn_first_page(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to turn pages", title="No pages found")
        else:
            self.current_page_num = 0
            self.update_records()

    def turn_last_page(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to turn pages", title="No pages found")
        else:
            pages = len(self.file.get_players_from_file()) // self.players_per_page
            self.current_page_num = pages
            self.update_records()


    def set_p_per_page(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to set quantity of players per page", title="No file found")
        else:
            value = self.players_p_page_var.get()
            self.players_per_page = int(value)
            self.update_records()

    def search_window(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to search for players", title="No file found")
        else:
            self.search_window = SearchWindow(self.root, self)

    def search_results(self, *values):
        search_criteria = SearchCriteria(*values)
        searched_players = self.file.get_players_by_criteria(search_criteria)
        if not searched_players:
            messagebox.showinfo("Search", "No players were found by the criteria you picked.")
            return
        else:
            SearchResultWindow(searched_players=searched_players)

    def add_player(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to add a new player", title="No file found")
        else:
            self.add_window = AddWindow(self.root, self)

    def delete_players(self):
        if self.file is None:
            messagebox.showwarning(message="It's seems, you didn't open any file to add a new player", title="No file found")
        else:
            self.add_window = DeleteWindow(self.root, self)



