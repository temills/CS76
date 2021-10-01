#!/usr/bin/env python3

from SensorlessProblem import SensorlessProblem
from Maze import Maze

#from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems
test_maze2 = Maze("maze2.maz")
test_sp = SensorlessProblem(test_maze2)

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_sp, null_heuristic)
print(result)

# better than null heuristic, but not optimistic
result = astar_search(test_sp, test_sp.sensorless_heuristic1)
print(result)

# optimistic heuristic, best option
result = astar_search(test_sp, test_sp.sensorless_heuristic)
print(result)
test_sp.animate_path(result.path)

# 20x20 maze with 20% walls
test_maze2 = Maze("maze9.maz")
test_sp = SensorlessProblem(test_maze2)
result = astar_search(test_sp, test_sp.sensorless_heuristic)
print(result)

# 30x30 maze
test_maze2 = Maze("maze10.maz")
test_sp = SensorlessProblem(test_maze2)
result = astar_search(test_sp, test_sp.sensorless_heuristic)
print(result)

