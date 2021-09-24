#!/usr/bin/env python3

from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

"""
print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))
"""
#Lossy version

problem4314 = FoxProblem((4, 3, 1, 4))
problem3313 = FoxProblem((3, 3, 1, 3))

print(bfs_search(problem3313))
print(dfs_search(problem3313))
print(ids_search(problem3313))

print(bfs_search(problem4314))
print(dfs_search(problem4314))
print(ids_search(problem4314))

