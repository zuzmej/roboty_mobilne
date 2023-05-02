from algorithm import algorithm
from maze_reader import maze_reader #do testów

## @brief Class containing right hand algorithm 
#

class right_hand(algorithm):

    ## @brief Constructor to initialize maze
    #
    # @param maze is a 2d list representing the layout of the walls in the maze from maze_reader
    def __init__(self, maze):
        self.maze = maze #przekazanie labiryntu z maze_reader
        self.path = [[0 for _ in range(16)] for _ in range(16)] # zainicjalizowanie listy dwuwymiarowej path zerami


    def right_hand_algorithm(self, position, end_position):
        start_north = self.NORTH
        start_right = self.EAST
        start_left = self.WEST
        start_south = self.SOUTH
        column = position[0]    # obecne położenie
        row = position[1]
        self.path[column][row] = 1     # wpisanie 1 do listy tam, gdzie znalazł się robot
        for i in range(7):
            if position != end_position:   # dopóki robot nie dotrze do końca ścieżki
                print("\nZaczynamy\n")
                if not self.maze[column][row] & self.EAST: #jeśli nie ma prawej ściany
                    column += 1                                 # "jedzie w prawo" -- zwiększa się kolumna
                    position = [column, row]
                    self.path[column][row] = 1     # zaznacza ścieżkę
                elif not self.maze[column][row] & self.NORTH:  #jest prawa ściana, ale nie ma przedniej
                    print("Tu nie ma przedniej ściany: ", position)
                    row += 1                                    # "jedzie do przodu" -- zwiększa się rząd
                    position = [column, row]
                    self.path[column][row] = 1
                elif not self.maze[column][row] & self.WEST:  #są prawa i przednia, ale nie ma lewej ściany
                    column -= 1                                    # "jedzie w lewo" -- zmniejsza się kolumna
                    position = [column, row]
                    self.path[column][row] = 1
                    print("position 3", position)
                elif not self.maze[column][row] & self.SOUTH: #są ściany prawa, przednia, lewa, ale nie ma tylnej
                    row -= 1                                       # "jedzie do tyłu" -- zmniejsza się rząd
                    position = [column, row]
                    self.path[column][row] = 1
                    print("position 4", position)
                print(position)
        return self.path
    


    def solve(self) -> list:
        column = 0
        row = 0
        position = [column, row]    # pole startowe [0,0]
        end_position = self.find_finish()   #pole końcowe
        self.right_hand_algorithm(position, end_position)   # wywołanie algorytmu prawej ręki
        for i in range(15,-1,-1):     # wypisanie wyznaczonej sciezki
            for j in range(16):
                print(self.path[j][i], end=" ")
            print("\n")

        return self.path
        




maze = maze_reader()
rh = right_hand(maze.read_maze("mazes/maze2"))
rh.solve()