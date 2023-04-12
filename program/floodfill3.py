from data import data
from algorithm import algorithm
from maze_reader import maze_reader

class floodfill(algorithm):
    INF = 2137
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
    def flood_fill(self, start_col, start_row, end_col, end_row,forbidden_direction,value): # pole startowe; pole końcowe (srodek labiryntu); kierunek w ktory nie można iść, wartość początkowa 
        current_col = start_col
        current_row = start_row
        cols_queue = []
        rows_queue = []
        values_queue = []
        fd_queue = []

        cols_queue.append(current_col)
        rows_queue.append(current_row)
        values_queue.append(value)
        fd_queue.append(forbidden_direction)
        
        
        
        while(current_col != end_col or current_row != end_row): # dopuki nie trafimy do środka labirynu
            current_col = cols_queue.pop(0)
            current_row = rows_queue.pop(0)
            value = values_queue.pop(0)
            forbidden_direction = fd_queue.pop(0)

            if(self.values[current_col][current_row] == self.INF):
                self.values[current_col][current_row] = value

                if(self.maze[current_col][current_row] & self.NORTH == 0 and self.NORTH != forbidden_direction):
                    cols_queue.append(current_col)
                    rows_queue.append(current_row + 1)
                    values_queue.append(value + 1)
                    fd_queue.append(self.SOUTH)

                if(self.maze[current_col][current_row] & self.SOUTH == 0 and self.SOUTH != forbidden_direction):
                    cols_queue.append(current_col)
                    rows_queue.append(current_row - 1)
                    values_queue.append(value + 1)
                    fd_queue.append(self.NORTH)

                if(self.maze[current_col][current_row] & self.WEST == 0 and self.WEST != forbidden_direction):
                    cols_queue.append(current_col - 1)
                    rows_queue.append(current_row)
                    values_queue.append(value + 1)
                    fd_queue.append(self.EAST)

                if(self.maze[current_col][current_row] & self.EAST  == 0 and self.EAST != forbidden_direction):
                    cols_queue.append(current_col + 1)
                    rows_queue.append(current_row)
                    values_queue.append(value + 1)
                    fd_queue.append(self.WEST)

    
   
    # znajduje minimalną wartość  w otoczeniu danego pola 
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
    def get_path(self,end_col, end_row,start_col, start_row):
        current_col = start_col
        current_row = start_row
        self.path[current_col][current_row] = 1
        while(current_col != end_col or current_row != end_row):
            [current_col, current_row] = self.find_smallest_value(current_col, current_row)
            self.path[current_col][current_row] = 1
            



            
         
         

    def solve(self):
        [end_col,end_row] = self.find_finish()
        self.flood_fill(0,0,end_col,end_row,self.EAST,0)
        self.get_path(0,0,end_col,end_row)
        # for i in range(15,-1,-1):   
        #     for j in range(16):
        #         print(self.path[j][i],end=" ")
        #     print("\n")
        
                