#!/usr/bin/env python3

from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = tuple([0] + maze.robotloc)
        self.num_robots = int(len(maze.robotloc)/2)


    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    # Returns list of state, cost pairs
    # Where states are states reachable from this point
    # And cost is transition cost of reaching that state from this point
    def get_successors(self, state):
        robot = state[0]
        #initialize list with option to stay put (0 cost)
        state_list = [(tuple([(robot + 1) * int(robot != (self.num_robots-1))] + list(state[1:])), 0)]

        #get robot to move's current location
        x = state[(robot*2)+1]
        y = state[(robot*2)+2]

        #get other robot locations - should keep track of this in maze object?
        robot_locs = []
        for i in range(1,len(state)-1,2):
            robot_locs.append((state[i],state[i+1]))

        #try out moves N,E,S,W
        for next_loc in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            #if floor of maze and no robot already there
            if self.maze.is_floor(next_loc[0],next_loc[1]) and (next_loc not in robot_locs):
                #get new state with updated location of moving robot
                next_state = [(robot + 1) * int(robot != (self.num_robots-1))]
                for i in range(1, len(state)):
                    if (i == (robot*2)+1):
                        next_state.append(next_loc[0])
                    elif  (i == (robot*2)+2):
                        next_state.append(next_loc[1])
                    else:
                        next_state.append(state[i])
                #add to state list with cost 1
                state_list.append((tuple(next_state), 1))
        return state_list

    # Returns true if all robots in correct locations
    # Returns false otherwise
    def goal_test(self, state):
        return(state[1:]==self.goal_locations)

    # Manhattan distance 
    def manhattan_heuristic(self, state):
        s = 0
        for i in range(1, len(state)-1):
            s = s + abs(state[i] - self.goal_locations[i-1])
        return s


    # Given a sequence of states (including robot turn), modify the maze and print it out.
    # (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
