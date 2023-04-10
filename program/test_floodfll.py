from data import data
from algorithm import algorithm
from maze_reader import maze_reader

from collections import deque

def flood_fill(maze, start, end):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    def in_bounds(x, y):
        return 0 <= x < 16 and 0 <= y < 16

    def neighbors(x, y):
        result = []
        if in_bounds(x, y - 1) and not (maze[y][x] & NORTH):
            result.append((x, y - 1))
        if in_bounds(x + 1, y) and not (maze[y][x] & EAST):
            result.append((x + 1, y))
        if in_bounds(x, y + 1) and not (maze[y][x] & SOUTH):
            result.append((x, y + 1))
        if in_bounds(x - 1, y) and not (maze[y][x] & WEST):
            result.append((x - 1, y))
        return result

    weights = [[float('inf')] * 16 for _ in range(16)]
    weights[start[1]][start[0]] = 0

    for _ in range(16 * 16):
        for y in range(16):
            for x in range(16):
                for nx, ny in neighbors(x, y):
                    new_weight = weights[y][x] + 1
                    if weights[ny][nx] > new_weight:
                        weights[ny][nx] = new_weight

    return weights




r = maze_reader()
maze = r.read_maze("mazes/maze2_50")
dist = flood_fill(maze,(0,0),(8,7))
for i in dist:
    print(i)
