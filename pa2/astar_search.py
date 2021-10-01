from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    cost = 0
    current = node
    while current:
        result.append(current.state)
        cost = cost + current.transition_cost
        current = current.parent
    result.reverse()
    return result, cost

# A* Search
# Searches through state space using heuristic function and transition cost between nodes
# Returns optimal solution path
def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0
    
    #go until solution found or frontier is empty
    while pqueue:
        node = heappop(pqueue)
        solution.nodes_visited = solution.nodes_visited + 1
        #if incorrect visited cost, node has been removed
        if node.parent != None:
            if visited_cost[node.state] != visited_cost[node.parent.state] + node.transition_cost:
                continue
        #return path if goal node found
        if search_problem.goal_test(node.state):
            solution.path, solution.cost = backchain(node)
            return solution
        #add successors to frontier
        for successor_tup in search_problem.get_successors(node.state):
            successor_state = successor_tup[0]
            transition_cost = successor_tup[1]
            cost = visited_cost[node.state]+transition_cost
            #create node
            successor = AstarNode(successor_state, heuristic_fn(successor_state), node, transition_cost)
            #cost = successor.priority()
            prev_cost = visited_cost.get(successor.state,-1)
            #add node to frontier
            if (prev_cost<0) or (cost < prev_cost): #either not already visited or better cost
                visited_cost[successor.state] = cost #functions as marking previous node with this state as removed
                heappush(pqueue, successor)
    return solution
