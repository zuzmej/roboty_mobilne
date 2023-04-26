from data import data
from algorithm import algorithm
from maze_reader import maze_reader



## @brief Class containing implementations of the floodfill algorithm
#
# 

class floodfill(algorithm):
    INF = 2137

    ## @brief Constructor
    #
    # @param _maze 2d list representing the layout of the walls in the maze 
    def __init__(self,_maze):
        self.maze = _maze
        self.values = [[self.INF for _ in range(16)] for _ in range(16)]
        self.path = [[0 for _ in range(16)] for _ in range(16)]

        # Opis działania:
        # 1. wepchnięcie na koniec kolejek początkowych współrzędnych, kierunku poruszania się i wartosći pola
        # 2. zdjęcie z początków kolejek współrzędnych (bieżąco rozpatrywanych), kierunku poruszania się(bieżąco rozpatrywanego) i wartosći pola (bieżąco rozpatrywanego)
        # 3. sprawdzenie czy w bierzącym polu jest już przypisana wartość
        #   3.1. jesli tak to powrót do 2.
        #   3.2. wpisanie wartości bieżącej do listy wartosći
        # 4. sprawdzenie jakie sąsiadujące kwadraty są osoiągalne
        # 5.wepchnięcie na koniec kolejek osiągalnych kwadratów, ich wartości  i kierunków poruszania się
        # 6. powrót do 2 dopuki nie osiągneliśmy końca labiryntu

    ## @brief Maze flooding algorithm 
    #
    # @details The algorithm starts flooding from the starting field (the field in which the robot is located at the beginning). 
    # Pouring is done in the direction of the center. The higher the value of a given field, the farther that field is from the start field. 
    #
    # @param start_col Column number describing the starting field
    # @param start_row Row number describing the starting field
    # @param end_col Column number describing the end field (center of the maze)
    # @param end_row Row number describing the end field (center of the maze)
    # @param forbidden_direction The direction in which you can not move (protects you from reversing the robot)
    # @param value Initial value from which flooding begins 


    def flood_fill(self, start_col, start_row, end_col, end_row,value): # pole startowe; pole końcowe (srodek labiryntu); kierunek w ktory nie można iść, wartość początkowa 
        current_col = start_col
        current_row = start_row
        cols_queue = []
        rows_queue = []
        values_queue = []

        cols_queue.append(current_col)
        rows_queue.append(current_row)
        values_queue.append(value)
        
        
        
        while(current_col != end_col or current_row != end_row): # dopuki nie trafimy do środka labirynu
            current_col = cols_queue.pop(0)
            current_row = rows_queue.pop(0)
            value = values_queue.pop(0)

            if(self.values[current_col][current_row] == self.INF):
                self.values[current_col][current_row] = value

                if(self.maze[current_col][current_row] & self.NORTH == 0):
                    cols_queue.append(current_col)
                    rows_queue.append(current_row + 1)
                    values_queue.append(value + 1)

                if(self.maze[current_col][current_row] & self.SOUTH == 0):
                    cols_queue.append(current_col)
                    rows_queue.append(current_row - 1)
                    values_queue.append(value + 1)

                if(self.maze[current_col][current_row] & self.WEST == 0):
                    cols_queue.append(current_col - 1)
                    rows_queue.append(current_row)
                    values_queue.append(value + 1)

                if(self.maze[current_col][current_row] & self.EAST  == 0):
                    cols_queue.append(current_col + 1)
                    rows_queue.append(current_row)
                    values_queue.append(value + 1)

    
   ## @brief Finds the field with the smallest value to which the robot can move
   #
   # @details Finds the field with the smallest value in the vicinity of the field in question, to which the robot can legally move
   #
   # @param start_col Column specifying the field in whose neighborhood we are looking for the smallest value 
   # @param end_col Row specifying the field in whose neighborhood we are looking for the smallest value 
   # @return Column and row describing the field with the smallest value 
    def find_smallest_value(self,start_col,start_row):
        cols = []
        rows = []
        values = []

        if(self.maze[start_col][start_row] & self.NORTH == 0):
            cols.append(start_col)
            rows.append(start_row + 1)
            values.append(self.values[start_col][start_row + 1])
            
        if(self.maze[start_col][start_row] & self.SOUTH == 0):
            cols.append(start_col)
            rows.append(start_row - 1)
            values.append(self.values[start_col][start_row - 1])
            
        if(self.maze[start_col][start_row] & self.WEST == 0):
            cols.append(start_col - 1)
            rows.append(start_row)
            values.append(self.values[start_col - 1][start_row])

        if(self.maze[start_col][start_row] & self.EAST  == 0):
            cols.append(start_col + 1)
            rows.append(start_row)
            values.append(self.values[start_col + 1][start_row])
           

        min_value = min(values)
        if(min_value > self.values[start_col][start_row]):
            return None
       
        index = values.index(min_value)
        current_col = cols.pop(index)
        current_row = rows.pop(index)
           
        cols.clear()
        rows.clear()
        values.clear()
        return [current_col,current_row]
            


            
        #wyznacza ścieżke 
    ## @brief Determines the path from the center of the maze to the starting field
    #
    # @details Determines a path by looking for the field with the smallest value in the neighborhood of the current field 
    # 
    # @param end_col Column number describing the starting field
    # @param end_row Row number describing the starting field
    # @param start_col Column number describing the end field
    # @param start_row Row number describing the end field
    def get_path(self,end_col, end_row,start_col, start_row):
        current_col = start_col
        current_row = start_row
        self.path[current_col][current_row] = 1
        while(current_col != end_col or current_row != end_row):
            [current_col, current_row] = self.find_smallest_value(current_col, current_row)
            self.path[current_col][current_row] = 1
            



            
         
         
    ## @brief  Method that performs all the steps necessary to determine the path 
    #
    # @return path Returns a 2d list representing the path from the start field to the end field.
    def solve(self):
        [end_col,end_row] = self.find_finish()
        self.flood_fill(0,0,end_col,end_row,0)
        self.get_path(0,0,end_col,end_row)
        for i in range(15,-1,-1):   
            for j in range(16):
                print(self.path[j][i],end="   ")
            print("\n")

        return self.path
        

mz = maze_reader()
f = floodfill(mz.read_maze("mazes/maze2_50"))
f.solve()
        
                