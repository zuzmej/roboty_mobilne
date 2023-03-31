from abc import ABC, abstractmethod
from data import data

class algorithm(data,ABC):
    # zdefiniowanie kierunków do określania ścian labiryntu
    NORTH = 1   #binarnie: 0001
    EAST = 2    #binarnie: 0010
    SOUTH = 4   #binarnie: 0100
    WEST = 8    #binarnie: 1000
    
    @abstractmethod
    def solve(self):
        pass

    def find_finish(self) -> list:  #metoda do znajdowania współrzędnych środkowego kwadratu
        finish_position = []
        for col in range(len(data.maze)-1):
            for row in range(len(data.maze[col])-1):
                if data.maze[col][row] & 0b1100 and data.maze[col][row+1] & 0b1001 and data.maze[col+1][row] & 0b0100 and data.maze[col+1][row+1] & 0b0011:   #pierwszy przypadek
                    pass    #finish position dodaj 4 współrzędne, nie wiem jak to zrobić z tymi listami ehh
                #if (...)    #drugi przypadek
                #if (...)    #trzeci przypadek