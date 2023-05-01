from abc import ABC, abstractmethod
from data import data
from maze_reader import maze_reader #do testów

class algorithm(data,ABC):
    # zdefiniowanie kierunków do określania ścian labiryntu
    NORTH = 1   #binarnie: 0001
    EAST = 2    #binarnie: 0010
    SOUTH = 4   #binarnie: 0100
    WEST = 8    #binarnie: 1000
    
    # @abstractmethod   #odkomentować po testach
    # def solve(self):
    #     pass

    def find_finish(self) -> list:  #metoda do znajdowania współrzędnych końca ścieżki
        finish_position = []
        walls_number = 0
        for col in range(len(self.maze)-1): #podwójna pętla -- po kolumnach i wierszach (do przedostatnich)
            for row in range(len(self.maze[col])-1):
                if not self.maze[col][row] & 0b0011 and not self.maze[col][row+1] & 0b0110 and not self.maze[col+1][row] & 0b1001 and not self.maze[col+1][row+1] & 0b1100:   #znalezienie dużego kwadratu - jeśli nie ma ścian wewnątrz
                    if self.maze[col][row] & self.WEST:     # zliczanie liczby ścian otaczających duży kwadrat
                        walls_number += 1
                    if self.maze[col][row] & self.SOUTH:
                        walls_number += 1
                    if self.maze[col][row+1] & self.WEST:
                        walls_number += 1
                    if self.maze[col][row+1] & self.NORTH:
                        walls_number += 1
                    if self.maze[col+1][row] & self.SOUTH:
                        walls_number += 1
                    if self.maze[col+1][row] & self.EAST:
                        walls_number += 1
                    if self.maze[col+1][row+1] & self.NORTH:
                        walls_number += 1
                    if self.maze[col+1][row+1] & self.EAST:
                        walls_number += 1
                    if walls_number == 7:       # jeżeli liczba ścian otaczających duży kwadrat jest równa dokładnie 7
                        if not self.maze[col][row] & self.WEST or not self.maze[col][row] & self.SOUTH:   #znalezienie które pole ma wjazd do środka i przypisanie tej wartości
                            finish_position = [col, row]
                        elif not self.maze[col][row+1] & self.NORTH or not self.maze[col][row+1] & self.WEST:
                            finish_position = [col, row+1]
                        elif not self.maze[col+1][row] & self.SOUTH or not self.maze[col+1][row] & self.EAST:
                            finish_position = [col+1, row]
                        elif not self.maze[col+1][row+1] & self.NORTH or not self.maze[col+1][row+1] & self.EAST:
                            finish_position = [col+1, row+1]
                    else:
                        pass
                    walls_number = 0
        return finish_position
    



maze = maze_reader()
maze.read_maze("mazes/maze_6_100")
s = algorithm()
print(s.find_finish())
