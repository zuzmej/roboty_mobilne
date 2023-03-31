from abc import ABC, abstractmethod
from data import data

# zdefiniowanie kierunków do określania ścian labiryntu
NORTH = 1   #binarnie: 0001
EAST = 2    #binarnie: 0010
SOUTH = 4   #binarnie: 0100
WEST = 8    #binarnie: 1000

class algorithm(data,ABC):
    
    @abstractmethod
    def solve(self):
        pass

# przykładowe użycie
west_south_east = 0x0E

if west_south_east & NORTH:
    print("Jest ściana północna")

if not west_south_east & NORTH:
    print("Nie ma ściany północnej")