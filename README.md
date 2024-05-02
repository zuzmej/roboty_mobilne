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
In the "program" subdirectory (cd roboty_mobilne/program):
```bash
python3 main.py
```

# Description
This simple application allows the user to choose a maze from the sample mazes (mazes directory), then choose the algorithm. After clicking "Play" button, the algorithm finds the shortest path from left bottom corner (start) to the middle of the maze. \
!**NOTE**
Right-hand rule does not guarantee finding the solution. In such situations, whenever right-hand algorithm cannot find the solution, the application freezes.

![choose_maze](https://github.com/zuzmej/roboty_mobilne/assets/101196834/f56ed78c-f1d5-405c-8411-3aaa6d73bfe8)
![choose_algorithm](https://github.com/zuzmej/roboty_mobilne/assets/101196834/e44637e8-2973-4364-8594-cf61ab571f9c)
![solved](https://github.com/zuzmej/roboty_mobilne/assets/101196834/d18c91ce-e78e-4360-a2ea-19c8580d4d44)

