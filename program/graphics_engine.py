from data import data
import tkinter as tk
from tkinter import ttk
import os   #operacje na plikach i katalogach

from maze_reader import maze_reader

class graphics_engine(data):

    NORTH = 1   #binarnie: 0001
    EAST = 2    #binarnie: 0010
    SOUTH = 4   #binarnie: 0100
    WEST = 8    #binarnie: 1000
    def __init__(self):
        self.window = tk.Tk()
        self.chosen_maze = tk.StringVar()
        self.chosen_algorithm = tk.StringVar()
        self.canva = tk.Canvas(self.window, width= 514,height=514)
        self.canva.pack()

        self.choose_maze_button = tk.Button(self.window, text="Wybierz labirynt:", command = self.open_selection_window_maze)
        self.choose_maze_button.pack()
        
        self.label_chosen_maze = tk.Label(self.window, text = "---")
        self.label_chosen_maze.pack()
        self.choose_algorithm_button = tk.Button(self.window, text="Wybierz algorytm:", command=self.open_selection_window_algorithm)
        self.choose_algorithm_button.pack()
        self.label_chosen_algorithm = tk.Label(self.window, text="---")
        self.label_chosen_algorithm.pack()
        self.play = tk.Button(self.window, text="Play")
        self.play.pack()
        

       

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
            print("jestjesm w ifie")
            given_window.destroy()  # zamknij okienko
            if chosen == self.chosen_maze:  # wpisywanie wybranej opcji do etykiety
                self.label_chosen_maze.config(text=chosen.get())
                print("jestjesm w ifie 2 ")
                self.draw_maze(chosen.get())
            if chosen == self.chosen_algorithm:
                self.label_chosen_algorithm.config(text=chosen.get())

    def run(self):
        self.window.mainloop()



    def draw_maze(self,filename):
        self.canva.delete("all")
        
        filename = "mazes/"+filename
        # line_n = self.canva.create_line(0,0,32,0,width=4)
        # line_s = self.canva.create_line(0,32,32,32,width=4)
        # line_e = self.canva.create_line(32,0,32,32,width=4)
        # line_w = self.canva.create_line(0,0,0,32,width=4)
        print(filename)

        maze_r = maze_reader()
        maze = maze_r.read_maze(filename)
        # print(maze)
        offset = 32
        for x in range(16):   
            for y in range(16):
                if(maze[x][y] & self.NORTH):
                    self.canva.create_line(0+x*offset, 0+(15-y)*offset, 32+x*offset, 0+(15-y)*offset,width=4)
                
                if(maze[x][y] & self.SOUTH):
                #    self.canva.create_line(x*offset, y*offset+offset, x*offset+offset, y*offset+offset,width=4)
                    self.canva.create_line(0+x*offset, 32+(15-y)*offset, 32+x*offset, 32+(15-y)*offset,width=4)
                    # self.canva.create_line(512-x*offset, 32+y*offset, 32+x*offset, 32+y*offset,width=4)

                    # self.canva.create_line(x+x*offset,y+y*offset,x*offset,y*offset,width=4)
                if(maze[x][y] & self.WEST):
                    self.canva.create_line(0+x*offset,0+(15-y)*offset,0+x*offset,32+(15-y)*offset,width=4)
                if(maze[x][y] & self.EAST):
                    self.canva.create_line(32+x*offset,0+(15-y)*offset,32+x*offset,32+(15-y)*offset,width=4)
           

    def draw_path(self):
        pass


apka = graphics_engine()
apka.run()