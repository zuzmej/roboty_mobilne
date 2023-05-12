from algorithm import algorithm
from maze_reader import maze_reader
import heapq

## @brief Class containing implementation of the Dijkstra algorithm
#
# 

class dijkstra(algorithm):

    ## @brief Constructor
    #
    # @param _maze 2d list representing the layout of the walls in the maze 
    def __init__(self,_maze):
        self.maze = _maze
        self.path = [[0 for _ in range(16)] for _ in range(16)]


    ## @brief Method to create graph from maze. Each field of the maze is a new vertex. Graph is a dictionary containing vertices and neighbouring fields.
    # 
    # @return graph 
    def create_graph(self):
        graph = {}
        for col in range(len(self.maze)): #podwójna pętla -- po kolumnach i wierszach (do przedostatnich)
            for row in range(len(self.maze[col])):
                if not self.maze[col][row] & self.WEST:
                    if (col, row) in graph:
                        graph[(col, row)].append((col-1, row))    #pojedyncza krotka do listy
                    else:
                        graph[(col, row)] = [(col-1, row)]  #lista krotek 
                if not self.maze[col][row] & self.NORTH:
                    if (col, row) in graph:
                        graph[(col, row)].append((col, row+1))    
                    else:
                        graph[(col, row)] = [(col, row+1)]  
                if not self.maze[col][row] & self.EAST:
                    if (col, row) in graph:
                        graph[(col, row)].append((col+1, row))    
                    else:
                        graph[(col, row)] = [(col+1, row)]
                if not self.maze[col][row] & self.SOUTH:
                    if (col, row) in graph:
                        graph[(col, row)].append((col, row-1))    #pojedyncza krotka do listy
                    else:
                        graph[(col, row)] = [(col, row-1)]  #lista krotek
        return graph


    ## @brief Dijkstra algorithm to estimate the shortest path from the beginning to the center of the maze
    #
    # @param graph returned from method create_graph
    # @param start (0,0) position
    # @param end of the maze
    # 
    # @return shortest_path

    def dijkstra(self, graph:dict, start:tuple, end:tuple):  
        visited_vertices = {vertex: False for vertex in graph}  
        distances = {vertex: float('inf') for vertex in graph}
        path = {vertex: None for vertex in graph}

        distances[start] = 0
        queue = [(0, start)]

        while queue:
            (distance, vertex) = heapq.heappop(queue)
            visited_vertices[vertex] = True

            if vertex == end:
                break

            for neighbor in graph[vertex]:
                new_distance = distance + 1  # assuming that the weight of each edge is 1

                if new_distance < distances[neighbor] and not visited_vertices[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = vertex
                    heapq.heappush(queue, (new_distance, neighbor))

        # path reconstruction
        vertex = end
        shortest_path = []
        while vertex is not None:
            shortest_path.append(vertex)
            vertex = path[vertex]

        shortest_path.reverse()
        return shortest_path


    ## @brief Determines the path from the center of the maze to the starting field
    #
    # @details Determines a path by looking for the field with the smallest value in the neighborhood of the current field 
    # 
    # @param shortest_path given from method dijkstra
    def get_path(self, shortest_path):
        for coords in shortest_path:
            col = coords[0]
            row = coords[1]
            self.path[col][row] = 1
        for i in range(15,-1,-1):   
            for j in range(16):
                print(self.path[j][i],end="   ")
            print("\n")


    ## @brief  Method that performs all the steps necessary to determine the path 
    #
    # @return path Returns a 2d list representing the path from the start field to the end field.
    def solve(self):
        finish_position = self.find_finish()
        graph = self.create_graph()
        shortest = self.dijkstra(graph, (0,0), (finish_position[0], finish_position[1]))
        self.get_path(shortest)
        return self.path
    

mz = maze_reader()
d = dijkstra(mz.read_maze("mazes/maze5_58"))
d.solve()
# shortest = d.dijkstra(d.create_graph(), (0,0), (7,8))
# d.get_path(shortest)

# tmp = 
# print(tmp[(1,6)])

