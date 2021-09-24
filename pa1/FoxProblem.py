"""
class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0) #0 chickens, 0 foxes, 0 boats on starting bank
        self.num_chickens = start_state[0]
        self.num_foxes = start_state[1]

    # get successor states for the given state
    def get_successors(self, state):
        move = 1-(2*state[2]) #-1 if boat on start side, +1 if on end side
        s1 = (state[0]+move, state[1], int(state[2]==0))        #move one chicken
        s2 = (state[0], state[1]+move,int(state[2]==0))         #move one fox
        s3 = (state[0]+(2*move), state[1], int(state[2]==0))    #move two chickens
        s4 = (state[0], state[1]+(2*move), int(state[2]==0))    #move two foxes
        s5 = (state[0]+move, state[1]+move, int(state[2]==0))   #move one chicken, one fox
        return list(filter(lambda s: self.legal_test(s), [s1, s2, s3, s4, s5]))


    #returns true if state is safe for chickens and is legal, false otherwise
    def legal_test(self, state):
        #negative or too many chickens
        if state[0] < 0 or state[0] > self.num_chickens:    return False
        #negative or too many foxes
        if state[1] < 0 or state[1] > self.num_foxes:       return False
        #more foxes than chickens on either side
        if (state[0] > 0 and state[0] < state[1]) or ((self.num_chickens - state[0]) > 0) and ((self.num_chickens - state[0]) < (self.num_foxes - state[1])):  return False
        return True

    #returns true if state is goal state, false otherwise
    def goal_test(self, state):
        return state==self.goal_state

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
"""
#Lossy version

class FoxProblem:
    def __init__(self, start_state=(3, 3, 1, 3),E=1):
        self.start_state = start_state
        self.num_chickens = start_state[0]
        self.num_foxes = start_state[1]
        self.E = E

    # get successor states for the given state
    def get_successors(self, state):
        #if boat on start side
        states = []
        if state[2]==1:
            s1 = (state[0]-1, state[1], 0, state[3])        #move one chicken
            s2 = (state[0], state[1]-1,0, state[3])         #move one fox
            s3 = (state[0]-2, state[1], 0, state[3])    #move two chickens
            s4 = (state[0], state[1]-2, 0, state[3])    #move two foxes
            s5 = (state[0]-1, state[1]-1, 0, state[3])   #move one chicken, one fox
            states = [s1, s2, s3, s4, s5]
        else:
            chickens_on_side = (state[3] - state[0])
            if chickens_on_side > 0:
                states.append((state[0]+1, state[1], 1, state[3]))        #move one chicken
                states.append((state[0]+1, state[1]+1, 1, state[3]))   #move one chicken, one fox
            if chickens_on_side > 1:
                states.append((state[0]+2, state[1], 1, state[3]))    #move two chickens
            states.append((state[0], state[1]+1,1, state[3]))         #move one fox
            states.append((state[0], state[1]+2, 1, state[3]))    #move two foxes
        succ = list(filter(lambda s_new: s_new!=None, [self.get_legal(s) for s in states]))
        return succ

    #returns state with updated E value if legal, None if not legal
    def get_legal(self, state):
        if state[0] < 0 or state[0] > state[3]:
            return None
        if state[1] < 0 or state[1] > self.num_foxes:
            return None
        if (state[0] > 0 and state[0] < state[1]):
            #if chickens can't be eaten return false
            if state[0] > self.E - (self.num_chickens - state[3]):
                return None
            #if chickens can be eaten, eat the chickens
            else:
                state = (0, state[1], state[2], state[3] - state[0])
                #self.E = self.E - state[0]
        #more foxes on end side
        if((state[3] - state[0]) > 0) and ((state[3] - state[0]) < (self.num_foxes - state[1])):
            #if chickens can't be eaten return false
            if (state[3] - state[0]) > self.E - (self.num_chickens - state[3]):
                return None
            #if chickens can be eaten, eat the chickens
            else:
                state = (state[0], state[1], state[2], state[0])
                #self.E = self.E - (state[3] - state[0])
        return state

    #returns true if state is goal state, false otherwise
    def goal_test(self, state):
        return (state[0]==0 and state[1]==0 and state[2]==0)


    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
