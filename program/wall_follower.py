# algorytm prawej ręki
from algorithm import algorithm
from abc import ABC, abstractmethod

class right_hand(algorithm):

    def __init__(self, maze):
        maze = maze #przekazanie labiryntu z maze_reader


    def solve(self) -> list:
        pass

tablica_a = [1,2,3]
tablica_b = [33, 23, 13]
maze_example = [tablica_a, tablica_b]
print("maze example: ", maze_example)

konstr = right_hand(maze_example)