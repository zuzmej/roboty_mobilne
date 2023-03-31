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
