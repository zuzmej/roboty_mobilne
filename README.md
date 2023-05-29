# Visualisation of maze search algorithms
The application is used to visualise the performance of maze search algorithms used in micromouse robots. Four algorithms are implemented: 

- right hand  
- floodfill
- weighted floodfill
- dijkstra

## Adding your own mazes

You can add your own mazes to test the performance of the algorithms, by adding the maze file to the mazes directory

### Maze format
The file should contain 256 numbers stored in hex format. Each hex number specifies what walls enclose given field of the maze 
-  NORTH WALL  = 1  / bin: 0001
-  EAST WALL  = 2   / bin: 0010
-  SOUTH WALL = 4  / bin: 0100
-  WEST WALL  = 8  / bin: 1000


Sample mazes can be found in the maze directory.

# Run
```bash
python3 main.py
```


