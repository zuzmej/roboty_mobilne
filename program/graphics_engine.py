from data import data
import tkinter as tk
from tkinter import ttk
import os   #operacje na plikach i katalogach

class graphics_engine(data):

    def __init__(self):
        self.window = tk.Tk()
        self.chosen_maze = tk.StringVar()
        self.chosen_algorithm = tk.StringVar()
        self.create_widgets()
        
    def create_widgets(self):
        choose_maze_button = tk.Button(self.window, text="Wybierz labirynt", command = self.open_selection_window_maze)
        choose_maze_button.pack()
        choose_algorithm_button = tk.Button(self.window, text=self.chosen_algorithm.get(), command=self.open_selection_window_algorithm)
        choose_algorithm_button.pack()

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
        option_combobox_maze.bind("<<ComboboxSelected>>", lambda event: self.close_window_after_choosing(window, self.chosen_maze))
        option_combobox_maze.pack()

    def option_choose_algorithm(self, window):
        selection_frame_algorithm = tk.Frame(window)
        selection_frame_algorithm.pack(padx=50, pady=50)
        label_maze = tk.Label(selection_frame_algorithm, text="Wybierz algorytm:")
        label_maze.pack()

        option_combobox_algorithm = ttk.Combobox(selection_frame_algorithm, textvariable = self.chosen_algorithm)
        option_combobox_algorithm['values'] = ('prawa ręka', 'zalewanie', 'ważone zalewanie', 'dijkstra')
        option_combobox_algorithm.bind("<<ComboboxSelected>>", lambda event: self.close_window_after_choosing(window, self.chosen_algorithm))
        option_combobox_algorithm.pack()

    def close_window_after_choosing(self, given_window, chosen):  # metoda do zamykania okienka z listą wybieralną po wybraniu opcji
        if chosen.get():   # jeśli opcja została wybrana
            given_window.destroy()  # zamknij okienko

    def run(self):
        self.window.mainloop()



    def draw_maze(self):
        pass
    def draw_path(self):
        pass


apka = graphics_engine()
apka.run()