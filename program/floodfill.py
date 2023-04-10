from data import data
from algorithm import algorithm
from maze_reader import maze_reader
import sys
import copy
import time
class floodfill(algorithm):

    def __init__(self,_maze):
        self.maze = _maze
        self.values = [[0 for _ in range(16)] for _ in range(16)]


    def find_first_move(self):
        maze_current_pos = self.find_finish()
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.SOUTH):
            if(self.maze[maze_current_pos[0] - 1][maze_current_pos[1] ] & self.SOUTH and self.maze[maze_current_pos[0]- 1][maze_current_pos[1] ] & self.WEST):
                maze_current_pos[0] = maze_current_pos[0] + 1
                maze_current_pos.append(self.WEST)
                return maze_current_pos 
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.SOUTH):
            if(self.maze[maze_current_pos[0]+ 1][maze_current_pos[1]] & self.SOUTH and self.maze[maze_current_pos[0]+ 1][maze_current_pos[1] ] & self.EAST):
                maze_current_pos[0] = maze_current_pos[0] - 1
                maze_current_pos.append(self.EAST)

                return maze_current_pos 
        
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.NORTH):
            if(self.maze[maze_current_pos[0]- 1][maze_current_pos[1] ] & self.NORTH and self.maze[maze_current_pos[0]- 1][maze_current_pos[1] ] & self.WEST):
                maze_current_pos[0] = maze_current_pos[0] + 1
                maze_current_pos.append(self.WEST)
                return maze_current_pos 
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.NORTH):
            if(self.maze[maze_current_pos[0]+ 1][maze_current_pos[1]] & self.NORTH and self.maze[maze_current_pos[0]+ 1][maze_current_pos[1] ] & self.EAST):
                maze_current_pos[0] = maze_current_pos[0] - 1
                maze_current_pos.append(self.EAST)
                return maze_current_pos 
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.WEST):
            if(self.maze[maze_current_pos[0]][ maze_current_pos[1] - 1] & self.WEST and self.maze[maze_current_pos[0]][maze_current_pos[1] - 1] & self.SOUTH):
                maze_current_pos[1] = maze_current_pos[1] + 1
                maze_current_pos.append(self.SOUTH)

                return maze_current_pos
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.WEST):
            if(self.maze[maze_current_pos[0]][maze_current_pos[1] + 1] & self.WEST and self.maze[maze_current_pos[0]][maze_current_pos[1] + 1] & self.NORTH):
                maze_current_pos[1] = maze_current_pos[1] - 1
                maze_current_pos.append(self.NORTH)

                return maze_current_pos
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.EAST):
            if(self.maze[maze_current_pos[0]][maze_current_pos[1] - 1] & self.EAST and self.maze[maze_current_pos[0]][maze_current_pos[1] - 1] & self.SOUTH):
                maze_current_pos[1] = maze_current_pos[1] + 1
                maze_current_pos.append(self.SOUTH)

                return maze_current_pos
            
        if(self.maze[maze_current_pos[0]][maze_current_pos[1]] & self.EAST):
            if(self.maze[maze_current_pos[0]][ maze_current_pos[1] + 1] & self.EAST and self.maze[maze_current_pos[0]][maze_current_pos[1] + 1] & self.NORTH):
                maze_current_pos[1] = maze_current_pos[1] - 1
                maze_current_pos.append(self.NORTH)

                return maze_current_pos
            


    def flood_fill(self,current_pos: list,forbidden_direction: int, value: int):
        #time.sleep(0.5)
        value = value + 1
        self.values[current_pos[0]][current_pos[1]] = value
        print(current_pos,end=" ")
        print(value)
        # for i in f.values:
        #     for j in i: 
        #         print(j,end=" ")
        #     print("\n")

        
        if((self.maze[current_pos[0]][current_pos[1]] & self.NORTH) == 0 and self.NORTH != forbidden_direction):
            current_pos[1] = current_pos[1] + 1
            if(self.values[current_pos[0]][current_pos[1]] == 0):
                self.flood_fill(current_pos ,self.SOUTH,value)

        if((self.maze[current_pos[0]][current_pos[1]] & self.SOUTH) == 0 and self.SOUTH != forbidden_direction):
            current_pos[1] = current_pos[1] - 1
            if(self.values[current_pos[0]][current_pos[1]] == 0):
                self.flood_fill(current_pos,self.NORTH,value)
        
        if((self.maze[current_pos[0]][current_pos[1]] & self.WEST) == 0 and self.WEST != forbidden_direction):
            current_pos[0] = current_pos[0] - 1
            if(self.values[current_pos[0]][current_pos[1]] == 0):
                self.flood_fill(current_pos,self.EAST,value)
        
        if((self.maze[current_pos[0]][current_pos[1]] & self.EAST) == 0 and self.EAST != forbidden_direction):
            current_pos[0] = current_pos[0] + 1
            if(self.values[current_pos[0]][current_pos[1]] == 0):
                self.flood_fill(current_pos,self.WEST,value)

        if(forbidden_direction & self.NORTH):
            if(current_pos[1] < 15):
                current_pos[1] = current_pos[1] + 1

        if(forbidden_direction & self.SOUTH):
            if(current_pos[1] > 0):
                current_pos[1] = current_pos[1] - 1

        if(forbidden_direction & self.WEST):
            if(current_pos[0] > 0):
                current_pos[0] = current_pos[0] - 1

        if(forbidden_direction & self.EAST):
            if(current_pos[0] < 15):
                current_pos[0] = current_pos[0] + 1



        print("slepy zaułek")

        
    def solve(self):
        start_pose = self.find_finish()
        self.values[start_pose[0]][start_pose[1]] = 0
        first_move = self.find_first_move()
        print(start_pose)
        # print(first_move)
        self.flood_fill(first_move,first_move[2],0)
        #print(self.values)


r = maze_reader()
maze = r.read_maze("mazes/maze2_50")
f = floodfill(maze)
sys.setrecursionlimit(100000)
f.solve()
for i in range(16):
    for j  in range(16):
        print(f.values[j][i],end= " ")
    print('\n')



    

