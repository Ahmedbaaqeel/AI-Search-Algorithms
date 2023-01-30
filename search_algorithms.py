import heapq
from node import Node


class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
        # add the items to the PQ
        for item in items:
            self.add(item)

    """ 
    Add item to PQ with priority-value given by call to priority_function 
    """

    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)

    """ 
    pop and return item from PQ with min priority-value
    """

    def pop(self):
        return heapq.heappop(self.pqueue)[1]

    """ gets number of items in PQ """

    def __len__(self):
        return len(self.pqueue)


def expand(problem, node):
    s = node.state
    children = []
    for action in problem.actions(s):
        newState = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, newState)
        children.append(Node(newState, node, action, cost))
    return children


def get_path_actions(node):
    path_actions = []
    if node is None:
        return []
    elif node.parent_node is None:
        return []
    else:
        while node.parent_node is not None:
            path_actions.insert(0, node.action_from_parent)
            node = node.parent_node
        return path_actions


def get_path_states(node):
    status = []
    if node is None:
        return []
    else:
        while node.parent_node is not None:
            status.insert(0, node.state)
            node = node.parent_node
        status.insert(0, node.state)
        return status


def best_first_search(problem, f):
    node = Node(problem.initial_state)
    frontier = PriorityQueue([node], priority_function=f)
    reached = {problem.initial_state: node}
    while frontier:
        front_node = frontier.pop()
        if problem.is_goal(front_node.state):
            return front_node
        for child in expand(problem, front_node):
            s = child.state
            if (s not in reached.keys()) or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return None


def best_first_search_treelike(problem, f):
    node = Node(state=problem.initial_state)
    frontier = PriorityQueue([node], priority_function=f)
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            frontier.add(child)
    return None


def breadth_first_search(problem, treelike=False):
    if treelike:
        return best_first_search_treelike(problem, lambda Node: Node.depth)
    else:
        return best_first_search(problem, lambda Node: Node.depth)


def depth_first_search(problem, treelike=False):
    if treelike:
        return best_first_search_treelike(problem, f=lambda Node: -Node.depth)
    else:
        return best_first_search(problem, f=lambda Node: -Node.depth)


def uniform_cost_search(problem, treelike=False):
    if treelike:
        return best_first_search_treelike(problem, f=lambda Node: Node.path_cost)
    else:
        return best_first_search(problem, f=lambda Node: Node.path_cost)


def greedy_search(problem, h, treelike=False):
    if treelike:
        return best_first_search_treelike(problem, f=lambda node: h(node))
    else:
        return best_first_search(problem, f=lambda node: h(node))


def astar_search(problem, h, treelike=False):
    if treelike:
        return best_first_search_treelike(problem, f=lambda node: h(node) + node.path_cost)
    else:
        return best_first_search(problem, f=lambda node:  h(node) + node.path_cost)