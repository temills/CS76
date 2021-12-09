#Constraint satisfaction problem class
#Tracey Mills, 10/21/21

class ConstraintSatisfactionProblem:

    def __init__(self, domain, constraints):
        self.domain = domain    #list of lists of values
        self.constraints = constraints  #dictionary where keys are pairs of vars, vals are lists of pairs of vals
        self.numVars = len(domain)

    def __str__(self):
        string =  "CSP: "
        return string

    #check that each 
    def check(self, assignment):
        #get each pair of assigned variables
        for i in range(len(assignment)):
            if assignment[i] == -1:
                continue
            v1 = assignment[i]
            for j in range(len(assignment)):
                if i == j or assignment[j] == -1:
                    continue
                v2 = assignment[j]
                #and check for consistency with constraints
                if i<j:
                    tup = (v1,v2)
                else:
                    tup = (v2,v1)
                if tup not in self.constraints[tuple(sorted([i,j]))]:
                    return False
        return True           