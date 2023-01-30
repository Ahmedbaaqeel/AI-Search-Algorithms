class Problem(object):

    def __init__(self, initial_state, goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        raise NotImplementedError()

    def result(self, state, action):
        raise NotImplementedError()

    def is_goal(self, state):
        return self.goal_state == state

    def action_cost(self, state1, action, state2):
        return 1

    def h(self, node):
        return 0


class RouteProblem(Problem):

    def __init__(self, initial_state, goal_state=None, map_graph=None, map_coords=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.map_graph = map_graph
        self.map_coords = map_coords

    def actions(self, state):
        neighbors = []
        for v1, v2 in self.map_graph:
            if v1 == state:
                neighbors.append(v2)

        return neighbors

    def result(self, state, action):
        for v1, v2 in self.map_graph:
            if v1 == state and v2 == action:
                return action
        return state  # No moves

    def action_cost(self, state1, action, state2):
        if (state1, state2) in self.map_graph:
            return self.map_graph[state1, state2]  # returning the cost of the action which is in the graph
        else:
            return 0

    def h(self, node):
        if node == self.goal_state:
            return 0
        else:  # Calc euclidean here
            (x1, y1) = self.map_coords[node.state]
            (x2, y2) = self.map_coords[self.goal_state]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)  # basic distance calculation
            return distance


class GridProblem(Problem):

    def __init__(self, initial_state, N, M, wall_coords, food_coords):
        food_eaten = []
        for i in range(0, len(food_coords)):
            food_eaten.append(False)
        food_eaten = tuple(food_eaten)
        self.N = N
        self.M = M
        self.initial_state = (initial_state, food_eaten)
        self.wall_coords = wall_coords
        self.food_coords = food_coords
        self.goal_state = None

    def actions(self, state):
        moves = []
        (x, y) = state[0]
        if x > 0 and y > 0:
            if (y + 1) <= self.N and (x, (y + 1)) not in self.wall_coords:
                moves.append("up")
            if (y - 1) >= 1 and (x, y - 1) not in self.wall_coords:
                moves.append("down")
            if (x + 1) <= self.M and (x + 1, y) not in self.wall_coords:
                moves.append("right")
            if (x - 1) >= 1 and (x - 1, y) not in self.wall_coords:
                moves.append("left")
        return moves

    def result(self, state, action):
        action_list = self.actions(state)
        if action not in action_list:
            return state  # if action is not possible
        x, y = state[0]
        if x > 0 and y > 0:
            if action == "up":
                y = y + 1
            if action == "down":
                y = y - 1
            if action == "right":
                x = x + 1
            if action == "left":
                x = x - 1
            new_coordinates = (x, y)
            food_eaten_tuple = state[1]
            if new_coordinates in self.wall_coords:
                return state

        if new_coordinates in self.food_coords:
            index = self.food_coords.index(new_coordinates)
            food_eaten_list = list(food_eaten_tuple)
            food_eaten_list[index] = True
            food_eaten_tuple = tuple(food_eaten_list)
            return (new_coordinates, food_eaten_tuple)
        else:
            return (new_coordinates, state[1])

    def action_cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        if False in state[1]:
            return False
        return True

    def h(self, node):
        distance = 99999999999  # Just so we put the first number and to make the for loop work
        x2, y2 = node.state[0]

        if self.is_goal(node.state):
            return 0
        else:
            for i in range(len(node.state[1])):
                if not node.state[1][i]:
                    x1, y1 = self.food_coords[i]
                    new_dist = abs(x1 - x2) + abs(y1 - y2)
                    if new_dist < distance:
                        distance = new_dist
            return distance
