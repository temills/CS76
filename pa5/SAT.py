# Tracey Mills 10/30/21
# GSAT and WalkSAT algorithms
import random
from resolution import resolution

class SAT():
    def __init__(self, cnf_file, do_resolution):
        #each row of cnf file has clause, with spaces between vars and - for negated vars
        #read file first to get list of variables, map to indexes for use in calculation
        all_vars = set()
        f = open(cnf_file, "r")
        for line in f:
            line_vars = str(line).split(" ")
            for v in line_vars:
                if(v=='' or v=='\n'):
                    break
                v = int(v)
                all_vars.add(abs(v))
        self.input_vars = [None] + sorted(list(all_vars)) #ignore index 0 since vars should have different +/- values
        self.vars = list(range(len(self.input_vars)))

        #clauses as lists of vars (negated if negative)
        clauses = []
        f = open(cnf_file, "r")
        for line in f:
            line_vars = str(line).split(" ")
            clause = []
            for v in line_vars:
                if(v=='' or v=='\n'):
                    break
                v = int(v)
                var = self.input_vars.index(abs(v))
                if v < 0:
                    var = -var
                clause.append(var)
            clauses.append(clause)
        self.clauses=clauses
        if do_resolution:
            print(len(self.clauses))
            while(True):
                new = resolution(self.clauses, self.vars)
                #no new clauses to add
                if len(new) == len(self.clauses):
                    break
                self.clauses = new
            print(len(self.clauses))
        self.h = 0.3
        self.max_iter = 1000000
        self.solution = None

    # Gsat algorithm
    # Sets self.solution to first solution found
    # Returns true if solution found, false if max_iter is reached before solution found
    def gsat(self):
        num_iter = 0
        #randomly initialize vars to true or false
        assignment = [None] + random.choices([True, False], [len(self.vars), len(self.vars)], k=len(self.vars)-1)
        
        #change assignment until all clauses satisfied
        while(not(self.check_assignment(assignment))):
            #print(self.count_satisfied(assignment))
            num_iter = num_iter+1
            if num_iter > self.max_iter:
                print("exceeded max iterations")
                return False

            #randomly choose variable to flip with probability 1-h
            if random.random() < self.h:
                i = random.randrange(1, len(assignment))
                assignment[i] = not(assignment[i])

            #flip var that satisfies most clauses with probability h
            else:
                counts = [None]
                #get num clauses satisfied when each var is switched
                for i in range(1, len(assignment)):
                    assignment[i] = not(assignment[i])
                    counts.append(self.count_satisfied(assignment))
                    assignment[i] = not(assignment[i])

                #randomly choose from all vars with max count
                max_indices = [i for i, v in enumerate(counts[1:]) if v == max(counts[1:])]
                i = random.choice(max_indices)+1
                assignment[i] = not(assignment[i])
        
        print(num_iter) 
        self.solution = assignment
        return True


    # Walksat algorithm
    # Sets self.solution to first solution found
    # Returns true if solution found, false if max_iter is reached before solution found
    def walksat(self):
        num_iter = 0
        #randomly initialize vars to true or false
        assignment = [None] + random.choices([True, False], [len(self.vars), len(self.vars)], k=len(self.vars)-1)
        
        #change assignment until all clauses satisfied
        while(not(self.check_assignment(assignment))):
            num_iter = num_iter+1
            if num_iter > self.max_iter:
                print("exceeded max iterations")
                return False

            #randomly choose variable to flip with probability h
            if random.random() < self.h:
                i = random.randrange(1, len(assignment))
                assignment[i] = not(assignment[i])

            #flip var that satisfies most clauses with probability 1-h
            else:
                counts = {}
                unsat = self.get_unsatisfied_clauses(assignment)
                clause = random.choice(unsat)
                
                #get num clauses satisfied when each var is switched
                for v in clause:
                    assignment[abs(v)] = not(assignment[abs(v)])
                    counts[abs(v)] = self.count_satisfied(assignment)
                    assignment[abs(v)] = not(assignment[abs(v)])

                #randomly choose from all vars with max count
                max_indices = [v for v, count in counts.items() if count == max(list(counts.values()))]
                i = random.choice(max_indices)
                assignment[i] = not(assignment[i])

        self.solution = assignment
        print(num_iter)
        return True

    # Returns true if all clauses are satisfied
    # False otherwise
    def check_assignment(self, assignment):
        for clause in self.clauses:
            satisfied = False
            #check if clause is satisfied (at least one var evaluates to true)
            for var in clause:
                #if negative var, check if false
                if var < 0:
                    if(not assignment[abs(var)]):
                        satisfied = True
                        break
                #if positive var, check if true
                else:
                    if(assignment[var]):
                        satisfied = True
                        break
            #if any clause not satisfied, return false
            if(not satisfied):
                return False
        #all clauses satisfied, return true
        return True


    # Returns number of currently satisfied clauses
    def count_satisfied(self, assignment):
        count = 0
        for clause in self.clauses:
            satisfied = False
            #check if clause is satisfied (at least one var evaluates to true)
            for var in clause:
                #if negative var, check if false
                if var < 0:
                    if(not assignment[abs(var)]):
                        satisfied = True
                        break
                #if positive var, check if true
                else:
                    if(assignment[var]):
                        satisfied = True
                        break
            #if clause satisfied, increase count
            if(satisfied):
                count = count+1
        #all clauses satisfied, return true
        return count


    # Returns list of all unsatisfied clauses
    def get_unsatisfied_clauses(self, assignment):
        clause_list = []
        for clause in self.clauses:
            satisfied = False
            #check if clause is satisfied (at least one var evaluates to true)
            for var in clause:
                #if negative var, check if false
                if var < 0:
                    if(not assignment[abs(var)]):
                        satisfied = True
                        break
                #if positive var, check if true
                else:
                    if(assignment[var]):
                        satisfied = True
                        break
            #if not satisfied, add to list
            if(not(satisfied)):
                clause_list.append(clause)
        #return list of unsatisfied clauses
        return clause_list


    # Writes file containing all vars set to True
    # One var per line
    def write_solution(self, filename):
        f = open(filename, "w")
        for i in range(1, len(self.solution)):
            if (self.solution[i]):
                f.write(str(self.input_vars[i]))
                f.write('\n')
        

