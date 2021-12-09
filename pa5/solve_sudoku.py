#!/usr/bin/env python3

from display import display_sudoku_solution
import random, sys
from SAT import SAT

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)
    
    puzzle_name = str(sys.argv[1][:-4])
    print(puzzle_name)
    sol_filename = puzzle_name + ".sol"

    do_resolution = False
    sat = SAT(sys.argv[1], do_resolution)

    #result = sat.gsat()
    result = sat.walksat()

    if result:
        sat.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)