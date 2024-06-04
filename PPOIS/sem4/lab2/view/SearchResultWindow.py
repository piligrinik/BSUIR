import tkinter as tk
from tkinter import ttk
from tkinter import Listbox

class SearchResultWindow(tk.Toplevel):
    def __init__(self,  searched_players):
        tk.Toplevel.__init__(self)
        self.searched_players = searched_players
        self.title('Search Results')
        self.geometry('800x400')
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=10)
        self.columnconfigure(index=0, weight=1)
        self.resizable(False, False)
        self.configure(background="#6E7B8B")
        self.__result_label: ttk.Label = ttk.Label(self, text='Search Result:', background=	"#6E7B8B")
        self.__result_label.grid(row=0, column=0)

        # count label

        self.__count_label: ttk.Label = ttk.Label(self, text=f'Found players quantity: {len(self.searched_players)}', background="#6E7B8B")
        self.__count_label.grid(row=0, column=0, sticky=tk.E)

        # result text panel

        self.__result_panel: ttk.Frame = ttk.Frame(self)
        self.__result_panel.rowconfigure(index=0, weight=1)
        self.__result_panel.columnconfigure(index=0, weight=1)
        self.__result_text: Listbox = Listbox(self.__result_panel,
                                              listvariable=tk.Variable(value=self.list_to_text_convert()), background="#BCD2EE")
        self.__result_text.grid(row=0, column=0, sticky=tk.NSEW)
        self.__result_panel.grid(row=1, column=0, sticky=tk.NSEW, columnspan=2)

    def list_to_text_convert(self):
        text: list = []
        for player in self.searched_players:
            text.append(player.get_player_info().__str__().strip())
        return text
