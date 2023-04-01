# algorytm prawej ręki
from algorithm import algorithm

class right_hand(algorithm):

    def __init__(self, maze):
        self.maze = maze #przekazanie labiryntu z maze_reader

    def solve(self) -> list:
        column = 0
        row = 0
        position = [column, row]    # pole startowe [0,0]
        self.path = [[0 for _ in range(16)] for _ in range(16)] # zainicjalizowanie listy dwuwymiarowej path zerami
        self.path[position[0]][position[1]] = 1     # wpisanie 1 do listy tam, gdzie znalazł się robot
        while position != self.find_finish():   # dopóki robot nie dotrze do końca ścieżki
            if not self.maze[position[0]][position[1]] & self.EAST: #jeśli nie ma prawej ściany
                column += 1                                 # "jedzie w prawo" -- zwiększa się kolumna
                position = [column, row]
                self.path[position[0]][position[1]] = 1     # zaznacza ścieżkę
            elif not self.maze[position[0]][position[1]] & self.NORTH:  #jest prawa ściana, ale nie ma przedniej
                row += 1                                    # "jedzie do przodu" -- zwiększa się rząd
                position = [column, row]
                self.path[position[0]][position[1]] = 1
            elif not self.maze[position[0]][position[1]] & self.WEST:  #są prawa i przednia, ale nie ma lewej ściany
                column -= 1                                    # "jedzie w lewo" -- zmniejsza się kolumna
                position = [column, row]
                self.path[position[0]][position[1]] = 1
            elif self.maze[position[0]][position[1]] & self.EAST and self.maze[position[0]][position[1]] & self.NORTH and self.maze[position[0]][position[1]] & self.WEST: #są ściany prawa, przednia, lewa
                row -= 1                                       # "jedzie do tyłu" -- zmniejsza się rząd
                position = [column, row]
                self.path[position[0]][position[1]] = 1
        return self.path



# chyba niepotrzebnie robię takie długie elify???
#dodac ograniczenia, zeby robo nie wyszedl poza labirynt!!!!!!!!!
# while(robot nie dotrze do konca sciezki){ 
#     if(nie ma sciany po prawej)             //* 
#         "ruszam sie w prawo" --- position[kolumna++][wiersz]
#         zaktualizuj path 
#     else if(można_jechać_prosto) 
#         // go
#     else if(można_skręcić_w_lewo)        //** 
#         skrec_w_lewo();                  //** 
#     else 
#         zawróć(); 
# jedz_jeden_segment_do_przodu(); 
# }

tablica_a = [10,10,10]
tablica_b = [10, 10, 10]
maze_example = [tablica_a, tablica_b]
print("maze example: ", maze_example)
konstr = right_hand(maze_example)

rh = right_hand(maze_example)
rh.solve()