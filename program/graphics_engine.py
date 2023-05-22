from data import data
import tkinter as tk
from tkinter import ttk
import os   #operacje na plikach i katalogach

class graphics_engine(data):

    def __init__(self):
        self.window = tk.Tk()
        self.chosen_maze = tk.StringVar()
        self.chosen_algorithm = tk.StringVar()

        self.label_chosen_maze = tk.Label(self.window, text = "---")
        self.label_chosen_maze.grid(row=0, column=1, padx=10, pady=10)

        self.label_chosen_algorithm = tk.Label(self.window, text="---")
        self.label_chosen_algorithm.grid(row=1, column=1, padx=10, pady=10)

        self.choose_maze_button = tk.Button(self.window, text="Wybierz labirynt:", command = self.open_selection_window_maze)
        self.choose_maze_button.grid(row=0, column=0, padx=10, pady=10) # choose_maze_button.pack()

        self.choose_algorithm_button = tk.Button(self.window, text="Wybierz algorytm:", command=self.open_selection_window_algorithm)
        self.choose_algorithm_button.grid(row=1, column=0, padx=10, pady=10) # choose_algorithm_button.pack()

    def open_selection_window_algorithm(self):
        selection_window_algorithm = tk.Toplevel(self.window)
        self.option_choose_algorithm(selection_window_algorithm)

    def open_selection_window_maze(self):
        selection_window_maze = tk.Toplevel(self.window) #tworzenie nowego okna do wybrania labiryntu
        self.option_choose_maze(selection_window_maze)

    def option_choose_maze(self, window):
        selection_frame_maze = tk.Frame(window)
        selection_frame_maze.pack(padx=50, pady=50)
        label_maze = tk.Label(selection_frame_maze, text="Wybierz labirynt:")  # etykieta 
        label_maze.pack()

        option_combobox_maze = ttk.Combobox(selection_frame_maze, textvariable = self.chosen_maze) #rozwijana lista (gdzie, do jakiej zmiennej)

        list_of_mazes = os.listdir("mazes") # pobranie nazw z folderu z labiryntami
        option_combobox_maze['values'] = list_of_mazes
        option_combobox_maze.bind("<<ComboboxSelected>>", lambda event: self.close_selection_window(window, self.chosen_maze))
        option_combobox_maze.pack()

    def option_choose_algorithm(self, window):
        selection_frame_algorithm = tk.Frame(window)
        selection_frame_algorithm.pack(padx=50, pady=50)
        label_maze = tk.Label(selection_frame_algorithm, text="Wybierz algorytm:")
        label_maze.pack()

        option_combobox_algorithm = ttk.Combobox(selection_frame_algorithm, textvariable = self.chosen_algorithm)
        option_combobox_algorithm['values'] = ('prawa ręka', 'zalewanie', 'ważone zalewanie', 'dijkstra')
        option_combobox_algorithm.bind("<<ComboboxSelected>>", lambda event: self.close_selection_window(window, self.chosen_algorithm))
        option_combobox_algorithm.pack()

    def close_selection_window(self, given_window, chosen):  # metoda do zamykania okienka z listą wybieralną po wybraniu opcji
        if chosen.get():   # jeśli opcja została wybrana
            given_window.destroy()  # zamknij okienko
            if chosen == self.chosen_maze:  # wpisywanie wybranej opcji do etykiety
                self.label_chosen_maze.config(text=chosen.get())
            if chosen == self.chosen_algorithm:
                self.label_chosen_algorithm.config(text=chosen.get())

    def run(self):
        self.window.mainloop()



    def draw_maze(self):
        pass
    def draw_path(self):
        pass


apka = graphics_engine()
apka.run()