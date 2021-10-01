#!/usr/bin/env python3

from MazeworldProblem import MazeworldProblem
from Maze import Maze

#from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0
"""
# Test problems
# 5x6 maze with 3 robots
# using null heuristic, aka uniform cost search
test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
print(test_mp.start_state)
result = astar_search(test_mp, null_heuristic)
print(result)
# Same maze with manhattan distance heuristic
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)

# 5 by 5 maze with 2 robots
# no walls, but robots must navigate around each other efficiently to switch positions
test_maze6 = Maze("maze6.maz")
test_mp = MazeworldProblem(test_maze6, (4,4,0,0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)

# 10 by 10 maze with 3 robots
# robots must squeeze out of tight corridor and reverse order before entering another tight corridor
test_maze4 = Maze("maze4.maz")
test_mp = MazeworldProblem(test_maze4, (9, 7, 9, 8, 9, 9))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)

# 20 by 20 maze with 3 robots
# robots must take turns squeezing through tunnel
# in order to switch sides of maze
test_maze7 = Maze("maze7.maz")
test_mp = MazeworldProblem(test_maze7, (19, 19, 0, 0, 0, 19))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)
"""
# 30 by 30 maze with 1 robot
# robot finds its way through lots of obstacles
# 1/3 of floor spaces are walls
# path found with less exploration since state space is smaller
test_maze8 = Maze("maze8.maz")
test_mp = MazeworldProblem(test_maze8, (0, 29))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)
"""
# 40 x 40 maze with 3 robots
# large maze with 20% walls
# still runs quickly
test_maze5 = Maze("maze5.maz")
test_mp = MazeworldProblem(test_maze5, (1, 0, 2, 0, 3, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
#test_mp.animate_path(result.path)
"""