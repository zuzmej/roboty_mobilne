from data import data

class maze_reader(data):

    def read_maze(self, maze_name: str) -> list:
        with open(maze_name) as maze_file:
            