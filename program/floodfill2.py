from data import data
from algorithm import algorithm
from maze_reader import maze_reader

class floodfill(algorithm):
    INF = 213700
    def __init__(self,_maze):
        self.maze = _maze
        self.values = [[self.INF for _ in range(16)] for _ in range(16)]


    def is_end(self, current_col, current_row, end_col, end_row):
        if(current_row == end_row and current_col == end_col):
            return True
        else:
            return False
        

    def flood_fill(self,current_col,current_row,end_col,end_row,forbidden_direction,value,stop):
        if(not self.is_end(current_col,current_row,end_col,end_row)):
            self.values[current_col][current_row] = value
            print(current_col,end=" ")
            print(current_row,end=" ")
            print(value)
            
        
            if((self.maze[current_col][current_row] & self.NORTH) == 0 and self.NORTH != forbidden_direction):
                current_row = current_row + 1
                if(self.values[current_col][current_row] == self.INF and not stop[0]):
                    stop = self.flood_fill(current_col,current_row,end_col,end_row,self.SOUTH,value + 1,stop)
            
            if((self.maze[current_col][current_row] & self.SOUTH) == 0 and self.SOUTH != forbidden_direction):
                current_row = current_row - 1
                if(self.values[current_col][current_row] == self.INF and not stop[0]):
                    stop = self.flood_fill(current_col,current_row,end_col,end_row,self.NORTH,value + 1,stop)

            if((self.maze[current_col][current_row] & self.WEST) == 0 and self.WEST != forbidden_direction):
                current_col = current_col - 1
                if(self.values[current_col][current_row] == self.INF and not stop[0]):
                    stop = self.flood_fill(current_col,current_row,end_col,end_row,self.EAST,value + 1,stop)
            
            if((self.maze[current_col][current_row] & self.EAST) == 0 and self.EAST != forbidden_direction):
                current_col = current_col + 1
                if(self.values[current_col][current_row] == self.INF and not stop[0]):
                    stop = self.flood_fill(current_col,current_row,end_col,end_row,self.WEST,value + 1,stop)
            if(stop[0] == False):
                self.values[current_col][current_row] = self.INF
                return [False]
            else:
                return [True]

        else:
            return [True]
        
    def solve(self):
        [end_col,end_row] = self.find_finish()
        self.flood_fill(0,0,end_col,end_row,self.SOUTH,0,[False])
r = maze_reader()
maze = r.read_maze("mazes/maze2_50")
f = floodfill(maze)
f.solve()
for i in f.values:
    print(i)

            