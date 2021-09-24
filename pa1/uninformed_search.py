from collections import deque
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0

# Breadth first search
# Returns solution object
def bfs_search(search_problem):
    s = search_problem.start_state
    sol = SearchSolution(search_problem, 'BFS')
    if search_problem.goal_test(s):
        sol.path = [s]
        sol.nodes_visited = 1
        return sol

    frontier = deque()
    frontier_states = set()
    frontier.append(SearchNode(s))
    visited = set()

    while True:
        if not(frontier):    #empty frontier means failure
            return sol
        
        node = frontier.popleft()
        visited.add(node.state)
        sol.nodes_visited = sol.nodes_visited + 1
        for successor in sorted(search_problem.get_successors(node.state), key=lambda s: (s[0]+s[1]), reverse=False):
            if (successor not in visited) and (successor not in [f.state for f in frontier]):
                successor_node = SearchNode(successor,node)
                if search_problem.goal_test(successor):
                    sol.path = backchain(successor_node)
                    return sol
                frontier.append(successor_node)

# Returns solution path list by backchaining through SearchNodes, starting with given node
def backchain(node):
    solution = deque()
    solution.appendleft(node.state)
    while(node.parent != None):
        node = node.parent
        solution.appendleft(node.state)
    return list(solution)


# Recursive depth first search with path checking
# Returns solution object
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    solution.nodes_visited = solution.nodes_visited + 1
    #return solution once goal is found
    if search_problem.goal_test(node.state):
        solution.path.append(node.state)
        if node.depth == 0:
            solution.path.reverse()
        return solution
    
    #base case
    if depth_limit==0:
        return solution

    #recursive case
    current_path = backchain(node)
    #sort successors so likely solutions explored first
    for successor in sorted(search_problem.get_successors(node.state), key=lambda s: (s[0]+s[1]), reverse=False):
        if successor not in current_path:     #pathchecking
            successor_node = SearchNode(successor,node)
            successor_node.depth = len(current_path)
            result = dfs_search(search_problem, depth_limit-1, successor_node, solution)
            #if succesfully found path
            if result.path != []:
                result.path.append(node.state)
                #reverse order of path once back at root
                if node.depth == 0:
                    result.path.reverse()
                return result
    
    #failure
    return solution

# Iterative deepening with depth first search
# Iteratively calls DFS with increasing depth limit until given limit is reached or goal is found
# Returns solution object
def ids_search(search_problem, depth_limit=100):
    solution = SearchSolution(search_problem, "IDS")
    #iterate through depths
    for depth in range(depth_limit):
        sol = dfs_search(search_problem, depth)
        #add nodes visited to count
        solution.nodes_visited = solution.nodes_visited + sol.nodes_visited
        #return solution if found
        if sol.path != []:
            solution.path = sol.path
            return solution
    return solution
