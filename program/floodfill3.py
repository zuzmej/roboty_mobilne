from data import data
from algorithm import algorithm
from maze_reader import maze_reader

class floodfill(algorithm):
    INF = 2137
    def __init__(self,_maze):
        self.maze = _maze
        self.values = [[self.INF for _ in range(16)] for _ in range(16)]
        self.path = [[0 for _ in range(16)] for _ in range(16)]

    def flood_fill(self, start_col, start_row, end_col, end_row,forbidden_direction,value):
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
        
        
        
        while(current_col != end_col or current_row != end_row):
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

    
   


    def get_path(self, start_col, start_row):
        pass
        # col = start_col
        # row = start_row
        # # value = self.values[col][row]
        # # self.path[col][row] = 1

        # # while(value):
        # #   [col,row] = self.one_less(col,row)
        # #   value = self.values[col][row]
        # #   self.path[col][row] = 1




            
         
         

    def solve(self):
        [end_col,end_row] = self.find_finish()
        self.flood_fill(0,0,end_col,end_row,self.EAST,0)
        self.get_path(end_col,end_row)

        for i in range(15,-1,-1):   
            for j in range(16):
                print(self.path[j][i],end=" ")
            print("\n")
        
            


r = maze_reader()
maze = r.read_maze("mazes/maze2_50")
f = floodfill(maze)

f.solve()

                
                       