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

    def find_finish(self) -> list:  #metoda do znajdowania współrzędnych końca ścieżki
        finish_position = []
        for col in range(len(self.maze)-1): #podwójna pętla -- po kolumnach i wierszach (do przedostatnich)
            for row in range(len(self.maze[col])-1):
                if not self.maze[col][row] & 0b0011 and not self.maze[col][row+1] & 0b0110 and not self.maze[col+1][row] & 0b1001 and not self.maze[col+1][row+1] & 0b1100:   #znalezienie dużego kwadratu
                    if not self.maze[col][row] & algorithm.WEST or not self.maze[col][row] & algorithm.SOUTH:   #znalezienie które pole ma wjazd do środka i przypisanie tej wartości
                        finish_position = [col, row]
                    elif not self.maze[col][row+1] & algorithm.NORTH or not self.maze[col][row+1] & algorithm.WEST:
                        finish_position = [col, row+1]
                    elif not self.maze[col+1][row] & algorithm.SOUTH or not self.maze[col+1][row] & algorithm.EAST:
                        finish_position = [col+1, row]
                    elif not self.maze[col+1][row+1] & algorithm.NORTH or not self.maze[col+1][row+1] & algorithm.EAST:
                        finish_position = [col+1, row+1]
                else:
                    pass
        return finish_position