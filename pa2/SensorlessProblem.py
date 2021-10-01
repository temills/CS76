from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.num_robots = int(len(maze.robotloc)/2)
        #start state includes all floor locations
        start_state = []
        for i in range(maze.width):
            for j in range(maze.height):
                if maze.is_floor(i,j):
                    start_state.append((i,j))
        l1 = sorted(list(start_state))
        l2 = []
        for t in l1:
            l2.append(t[0])
            l2.append(t[1])
        self.start_state = tuple(l2)
        #self.start_state = tuple(sorted(start_state))

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    # Returns list of state, cost pairs
    # Where states are states reachable from current possible states
    # And cost is transition cost of reaching that state from this point
    def get_successors(self, state):
        all_states = []
        #try out moves N,E,S,W
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            next_states = set()
            #move in given direction from all current states
            #for s in state:
            for k in range(0, len(state)-1, 2):
                x=state[k]
                y=state[k+1]
                #x = s[0]
                #y = s[1]
                next_loc = (x+i, y+j)
                #moves to next location
                if self.maze.is_floor(next_loc[0],next_loc[1]):
                    next_states.add(next_loc)
                #or stays put
                else:
                    #next_states.add(s)
                    next_states.add((x,y))
            l1 = sorted(list(next_states))
            l2 = []
            for t in l1:
                l2.append(t[0])
                l2.append(t[1])
            all_states.append((tuple(l2), 1))
            #all_states.append((tuple(sorted(list(next_states))),1))
        return all_states

    # Returns true if all robots in correct locations
    # Returns false otherwise
    def goal_test(self, state):
        #print(state)
        return len(state)==2

    # Heuristic for choosing next state
    # Total number of possible locations in current state
    # Not optimistic
    def sensorless_heuristic1(self, state):
        return len(state)

    # Heuristic for choosing next state
    # Sum of number of possible x positions -1 and number of possible y positions -1
    # Optimistic
    def sensorless_heuristic(self, state):
        xs = set()
        ys = set()
        for i in range(0, len(state)-1, 2):
            xs.add(state[i])
            ys.add(state[i+1])
        return len(xs) + len(ys) - 2


    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
