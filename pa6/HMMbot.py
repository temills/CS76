# Tracey Mills 11/15/2021
# This file contains the HMMbot class
# HMMbot uses probabilistic reasoning and filtering to compute probabile location in given maze

import numpy as np

class HMMbot:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze #is_floor and get_color
        #start state includes all floor locations
        locs = []
        for i in range(maze.width):
            for j in range(maze.height):
                if maze.is_floor(i,j):
                    locs.append((i,j))
        self.locs = tuple(sorted(locs))
        self.distr = []
        for i in range(len(self.locs)):
            self.distr.append(1/len(self.locs))


    # Updates probability distribution given random move and subsequent color sensed
    def step(self, color):
        transition_model = np.array(self.get_transition_model()).T
        sensor_model = np.array(self.get_sensor_model(color))
        current_distr = np.array(self.distr).T
        new_distr = np.dot((np.dot(sensor_model, transition_model)), current_distr)
        self.distr = self.normalize_distr(new_distr)


    # Returns transition model T
    # SxS matrix where S is number of locations
    # T[i][j] = prob of transitioning from loc i to loc j
    # Predicts prob distribution of current location after robot movement
    # Returns new distribution
    def get_transition_model(self):
        T = []
        #for each starting location
        for i in range(len(self.locs)):
            loc1 = self.locs[i]
            T.append([])
            #for each possible location
            for j in range(len(self.locs)):
                loc2 = self.locs[j]
                prob = 0
                #find probability of moving from loc1 to loc2
                for dir in ["N", "E", "S", "W"]:
                    #prob increases by 0.25 if a move in some direction takes us from loc1 to loc2
                    if self.make_given_move(loc1, dir) == loc2:
                        prob = prob + 0.25
                T[i].append(prob)
        return T
    
    
    # Returns sensor model O
    # SxS diagonal matrix where S is number of locations
    # O[i][i] = prob of given evidence (color) being sensed at location i
    def get_sensor_model(self, color):
        O = []
        for i in range(len(self.locs)):
            loc = self.locs[i]
            O.append([0]*len(self.locs))
            O[i][i] = self.sense_prob(loc, color)
        return O


    # Returns new location given current location and direction of attempted movement
    def make_given_move(self, loc, dir):
        #make sure valid location and direction
        if not(self.maze.is_floor(loc[0], loc[1])) or (dir not in ["N", "S", "E", "W"]):
            return None
        
        #update location depending on direction of attempted movement
        if dir=="N":
            new_loc = (loc[0], loc[1]+1)
        elif dir=="E":
            new_loc = (loc[0]+1, loc[1])
        elif dir=="S":
            new_loc = (loc[0], loc[1]-1)
        else:
            new_loc = (loc[0]-1, loc[1])

        #return new location if able to move there
        if self.maze.is_floor(new_loc[0], new_loc[1]):
            return new_loc
        #return same location as before if not able to move
        else:
            return loc
    

    # Normalizes distribution so probabilities sum to 1
    # Returns new distribution
    def normalize_distr(self, distr):
        tot = sum(distr)
        return [p/tot for p in distr]


    # Returns probability of sensing given color if at given location
    def sense_prob(self, loc, color):
        if self.maze.get_color(loc[0],loc[1]) == color:
            return 0.88
        else:
            return 0.04


    # Prints maze with probability distribution superimposed
    def print_distr(self):
        s=""
        for y in range(self.maze.height - 1, -1, -1):
            for x in range(self.maze.width):
                if(self.maze.is_floor(x,y)):
                    n = str(round(self.distr[self.locs.index((x,y))],2))[1:]
                    while(len(n)<3):
                        n = n + "0"
                    s+= n

                else:
                    s+= " # "
            s += "\n"
        print(s)
    
    # Prints state of maze, with robot at given loc
    def print_maze(self, loc):
        s=""
        for y in range(self.maze.height - 1, -1, -1):
            for x in range(self.maze.width):
                if(x==loc[0] and y==loc[1]):
                    s += " @ "
                elif(self.maze.is_floor(x,y)):
                    s+= " "+self.maze.get_color(x,y)+" "
                else:
                    s+= " # "
            s += "\n"
        print(s)