class Node(object):

    def __init__(self, state, parent_node=None, action_from_parent=None, path_cost=0):
        self.state = state
        self.parent_node = parent_node
        self.action_from_parent = action_from_parent
        self.path_cost = path_cost

        if self.parent_node is None:
            self.depth = 0
        else:
            self.depth = parent_node.depth + 1

    def __lt__(self, other):
        return self.state < other.state
