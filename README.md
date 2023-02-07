# AI-Search-Algorithms

This project uses various Artificial Intelligence search algorithms (Tree like or Graph like) to solve given problems.

## <img src="https://cdn-icons-png.flaticon.com/128/4236/4236694.png" style="width:30px;height:30px;"> Implementation :

## <p style="display: flex; justify-content: center;align-items:center;">Python<a href="https://www.python.org"><img src="https://cdn-icons-png.flaticon.com/128/919/919852.png" alt="Python logo" style="width:48px;height:48px;margin-left:10px;"> </a></p>

## <img src="https://cdn-icons-png.flaticon.com/128/8915/8915520.png" style="width:30px;height:30px;"> Search algorithms :

- Best-First-Search
- Breadth-First-Search
- Depth-First-Search
- Uniform-Cost-Search
- Greedy-Search
- A-Star-Search

## <img src="https://cdn-icons-png.flaticon.com/128/1011/1011812.png" style="width:30px;height:30px;"> Heuristics:

- Manhattan distance: |x1 - x2| + |y1 - y2|
- Eucledian distance: √(∑i=1N (pi-qi)²)

## <img src="https://cdn-icons-png.flaticon.com/128/9537/9537313.png" style="width:30px;height:30px;"> Problems :

- <b>Route problem</b>:
To clarify the usage of RouteProblem, consider the following map of cities.
<br>
  <img src="/extra-doc/route_example.PNG" width=350px>

Assume that start state is A, and the goal is E, assume all costs are 1. Then starting from A you have, giving one to the action function with the current state creates the new state. Furthermore, leading to E with the least cost using <b>Euclidean Distance</b> heuristic.
<br>


- <b>Grid problem</b>: A grid problem instance consists of an N-by-M grid (N rows and M columns). Some grid locations contain walls that the agent
cannot move into; we will use a list of locations wall_coords to store these wall locations. Some grid locations contain food
that the agent can consume food_coords. The agent starts at some grid location (xA, yA). The agent can move left, right, up,
and down one grid. The agent cannot move outside the bounds of the N-by-M grid. The goal is to consume all food on the grid with the minimum distance moved using <b>Manhattan distance</b> heuristic.

<img src="/extra-doc/grid_example.PNG" alt="Grid example" width=350px >

The agent is in (7, 4). The walls are at [(4,3), (5,1), (5,2)]. The food are at [(3,1), (2,3), (4,5)].

## <img src="https://cdn-icons-png.flaticon.com/128/2570/2570287.png" width=20px/> Author

[@AhmadBaaqeel](https://github.com/Ahmedbaaqeel)**
